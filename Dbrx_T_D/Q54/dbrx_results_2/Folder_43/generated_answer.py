from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[89] if len(t) > 89 else 10 ** 100
    primes = []
    for num in range(1, x):
        while num > 0:
            if not isprime(num):
                break
            num = num // 10
            if num == 0:
                primes.append(num)
                break
    return sorted(primes, reverse=True)