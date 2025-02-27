from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[945]
    primes = []
    for i in range(2, x):
        if isprime(i):
            trunc = i
            while trunc != 0:
                if not isprime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)