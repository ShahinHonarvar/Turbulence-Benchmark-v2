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
    return [int(left_truncate), int(right_truncate)]

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num < 10:
            continue
        is_truncatable = True
        left, right = left_right_truncate(num)
        while len(str(num)) > 2:
            if not is_prime(num) or not is_prime(left) or (not is_prime(right)):
                is_truncatable = False
                break
            num, left, right = left_right_truncate(num)
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)