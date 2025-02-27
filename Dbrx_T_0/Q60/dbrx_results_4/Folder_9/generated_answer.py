from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[29]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    ltrunc_primes = [i for i in primes if all((isprime(int(str(i)[j:])) for j in range(1, len(str(i)))))]
    rtrunc_primes = [i for i in primes if all((isprime(int(str(i)[:j])) for j in range(len(str(i)), 0, -1)))]
    lrtrunc_primes = [i for i in ltrunc_primes if i in rtrunc_primes]
    return sorted(lrtrunc_primes, reverse=True)