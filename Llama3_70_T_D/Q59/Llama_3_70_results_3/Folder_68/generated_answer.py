import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt_num = math.isqrt(num)
    for i in range(3, sqrt_num + 1, 2):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[1]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_left_truncatable = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes