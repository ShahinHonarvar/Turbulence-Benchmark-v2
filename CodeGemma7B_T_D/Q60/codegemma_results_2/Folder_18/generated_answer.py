from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if n % 10 == 0 or n % 10 == 5:
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        left = int(str_n[i:])
        right = int(str_n[:i])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[429]
    prime_list = [n for n in nums if is_prime(n)]
    truncatable_primes = []
    for prime in prime_list:
        if prime > x:
            continue
        if is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes