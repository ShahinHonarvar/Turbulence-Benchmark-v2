from sympy import isprime

def all_right_truncatable_prime(tp):
    x = tp[30]
    rt_primes = []
    for i in reversed(range(2, x)):
        digits = list(str(i))
        if isprime(int(''.join(digits))) and all((isprime(int(''.join(digits[:p]))) for p in range(1, len(digits)))):
            rt_primes.append(i)
    return sorted(rt_primes, reverse=True)