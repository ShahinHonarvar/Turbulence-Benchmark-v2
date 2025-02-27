from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def left_truncatable_prime(n):
    while n > 1:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def right_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n) - 1):
        n = int(str_n[:i] + str_n[i + 1:])
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[803]
    primes = []
    for n in range(2, x + 1):
        if is_prime(n) and left_truncatable_prime(n) and right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes)