from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[466]
    rt_primes = []
    for i in range(1, x):
        if isprime(i):
            is_rt_prime = True
            while i > 1:
                if not isprime(i):
                    is_rt_prime = False
                    break
                i = int(str(i)[:-1])
            if is_rt_prime:
                rt_primes.append(i)
    return sorted(rt_primes, reverse=True)