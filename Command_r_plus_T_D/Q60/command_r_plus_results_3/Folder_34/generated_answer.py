def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    str_num = str(num)
    left_trunc = str_num[1:] if len(str_num) > 1 else ''
    right_trunc = str_num[:-1] if len(str_num) > 1 else ''
    return is_prime(int(str_num)) and is_prime(int(left_trunc)) and is_prime(int(right_trunc))

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num > 1 and left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)