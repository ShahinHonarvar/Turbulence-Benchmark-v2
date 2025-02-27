from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[758]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    ltrunc_primes = [i for j, i in enumerate(primes) if isprime(int(str(i)[1:])) and isprime(int(str(i)[:-1]))]
    rtrunc_primes = [i for j, i in enumerate(primes) if isprime(int(str(i)[1:])) and isprime(int(str(i)[:-1]))]
    lrtrunc_primes = [i for i in ltrunc_primes if i in rtrunc_primes]
    return sorted(list(set(lrtrunc_primes)))