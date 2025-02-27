import sympy

def all_right_truncatable_prime(t):
    x = t[98]
    rt_primes = []
    for num in range(2, x):
        if sympy.isprime(num):
            trunc_num = num
            while trunc_num > 0:
                trunc_num //= 10
                if not sympy.isprime(trunc_num):
                    break
            else:
                rt_primes.append(num)
    return sorted(rt_primes)