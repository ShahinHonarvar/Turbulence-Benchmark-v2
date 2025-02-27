import sympy

def is_prime_truncatable(n):
    if '0' in str(n):
        return False
    s = str(n)
    for i in range(1, len(s)):
        if not sympy.isprime(int(s[i:])) or not sympy.isprime(int(s[:len(s) - i])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[23]
    truncatable_primes = []
    for i in range(2, x + 1):
        if sympy.isprime(i) and is_prime_truncatable(i):
            truncatable_primes.append(i)
    return truncatable_primes