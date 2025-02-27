from sympy import isprime

def all_right_truncatable_prime(positive_integers_tuple):
    x = positive_integers_tuple[803]
    right_truncatable_primes = []
    for n in range(2, x):
        if isprime(n):
            r = n
            while len(str(r)) > 1:
                r = int(str(r)[-1])
                if not isprime(r):
                    break
                else:
                    right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes)