def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncate(num):
    str_num = str(num)
    left_truncate = str_num
    right_truncate = str_num
    for _ in range(len(str_num) - 1):
        left_truncate = left_truncate[1:]
        if not is_prime(int(left_truncate)):
            break
    for _ in range(len(str_num) - 1):
        right_truncate = right_truncate[:-1]
        if not is_prime(int(right_truncate)):
            break
    return (left_truncate, right_truncate)

def all_left_right_truncatable_prime(num_tuple):
    truncatable_primes = []
    for num in range(num_tuple[0], num_tuple[1] + 1):
        if '0' in str(num):
            continue
        left, right = left_right_truncate(num)
        if left == '1' or left == '2' or left == '3' or (left == '5') or (left == '7'):
            if right == '1' or right == '3' or right == '7' or (right == '9'):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)