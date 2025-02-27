def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncate(num):
    str_num = str(num)
    left_truncate = str_num[1:] if len(str_num) > 1 else ''
    right_truncate = str_num[:-1] if len(str_num) > 1 else ''
    return (str_num, left_truncate, right_truncate)

def all_left_right_truncatable_prime(numbers):
    left_right_primes = []
    for num in numbers:
        if num < 2:
            continue
        current_num = num
        while current_num > 0:
            if not is_prime(current_num):
                break
            current_num, _, _ = left_right_truncate(current_num)
        if current_num == 0:
            left_right_primes.append(num)
    return sorted(left_right_primes, reverse=True)