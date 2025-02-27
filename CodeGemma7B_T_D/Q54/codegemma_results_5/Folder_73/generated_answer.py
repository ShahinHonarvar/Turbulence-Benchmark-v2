from sympy import isprime

def all_right_truncatable_prime(x):
    primes = []
    for num in range(2, x):
        if isprime(num):
            truncatable = True
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[:-i])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes)