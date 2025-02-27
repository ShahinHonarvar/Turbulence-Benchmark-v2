from sympy import isprime

def all_right_truncatable_prime(r: tuple) -> list:
    x = r[1]
    primes = []
    for i in range(10, x):
        if isprime(i):
            is_right_truncatable = True
            for j in range(len(str(i))):
                if not isprime(int(str(i)[:-j])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)