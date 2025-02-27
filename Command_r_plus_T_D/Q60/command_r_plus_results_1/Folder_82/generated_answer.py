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

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num < 10:
            continue
        left, right = left_right_truncate(num)
        if left == '2' or left == '3' or left == '5' or (left == '7'):
            if right == '2' or right == '3' or right == '5' or (right == '7'):
                truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes