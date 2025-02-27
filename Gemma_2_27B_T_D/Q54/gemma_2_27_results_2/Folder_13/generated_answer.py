from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[784]
    primes = []
    for i in range(2, x):
        if isprime(i):
            is_truncatable = True
            n = str(i)
            while len(n) > 1:
                n = n[:-1]
                if not isprime(int(n)):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes)