def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        left_trunc = str_num[i:]
        right_trunc = str_num[:i]
        if not is_prime(int(left_trunc)) or not is_prime(int(right_trunc)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    max_val = numbers[64]
    truncatable_primes = []
    for num in range(2, max_val + 1):
        if left_right_truncatable_prime(num) and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)