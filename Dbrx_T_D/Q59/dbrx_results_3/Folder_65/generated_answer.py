from sympy import isprime

def all_left_truncatable_prime(t):
    primes = []
    for i in range(10, t[32]):
        if isprime(i):
            is_left_truncatable = True
            for j in range(1, len(str(i))):
                if not isprime(int(str(i)[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes)