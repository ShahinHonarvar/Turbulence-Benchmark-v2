from sympy import isprime

def truncate_left(n):
    while n > 10:
        n = int(str(n)[1:])
        if not isprime(n):
            return False
    return True

def truncate_right(n):
    while n > 10:
        n = int(str(n)[:-1])
        if not isprime(n):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[46]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    truncatable_primes = [i for i in primes if truncate_left(i) and truncate_right(i)]
    return sorted(list(set(truncatable_primes)), reverse=True)