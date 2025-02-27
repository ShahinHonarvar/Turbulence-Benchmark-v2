from sympy import isprime

def is_truncatable_prime(num):
    if '0' in str(num):
        return False
    s = str(num)
    for i in range(1, len(s)):
        if not isprime(int(s[i:])) or not isprime(int(s[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    if len(nums) <= 86:
        return []
    x = nums[86]
    truncatable_primes = []
    for num in range(10, x + 1):
        if isprime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes