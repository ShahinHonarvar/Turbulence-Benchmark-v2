import sympy

def is_left_truncatable_prime(n):
    if '0' in str(n) or not sympy.isprime(n):
        return False
    while n > 0:
        n = int(str(n)[1:]) if len(str(n)) > 1 else 0
        if n and (not sympy.isprime(n)):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[70]
    result = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    result.sort(reverse=True)
    return result