from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[71]
    primes = []
    for i in range(x - 1, 1, -1):
        if isprime(i):
            num = i
            while num > 1:
                num = int(num / 10)
                if not isprime(num):
                    break
                    if num == 1 and i not in primes:
                        primes.append(i)
    return sorted(primes, reverse=True)