from sympy import isprime

def all_left_truncatable_prime(t):
    primes = []
    for i in range(1, 10):
        if isprime(i):
            primes.append(i)
        for j in range(len(primes)):
            num = i * 10 + primes[j]
            if isprime(num) and num < t[31]:
                primes.append(num)
    return sorted(list(set(primes)), reverse=True)