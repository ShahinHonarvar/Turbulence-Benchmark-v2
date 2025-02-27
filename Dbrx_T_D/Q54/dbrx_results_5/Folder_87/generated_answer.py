from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[39]
    primes = []
    for i in range(1, x):
        if isprime(i):
            is_right_truncatable = True
            for j in range(len(str(i))):
                if not isprime(int(str(i)[:-j])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    primes.sort(reverse=True)
    return primes