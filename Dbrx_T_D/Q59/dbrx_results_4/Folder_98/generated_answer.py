from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[8]
    primes = []
    for i in range(2, x):
        if isprime(i):
            is_left_truncatable = True
            for j in range(len(str(i))):
                if not isprime(int(str(i)[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    primes.sort(reverse=True)
    return primes