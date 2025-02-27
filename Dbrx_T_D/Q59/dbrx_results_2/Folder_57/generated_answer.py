from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[54]
    primes = []
    for num in range(1, x):
        if isprime(num):
            is_left_truncatable = True
            for i in range(len(str(num))):
                if not isprime(int(str(num)[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)