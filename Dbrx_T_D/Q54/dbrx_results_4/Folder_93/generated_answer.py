from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[11]
    primes = []
    for i in range(1, 10):
        if isprime(i) and i < x:
            primes.append(i)
    for i in range(10, x):
        num = i
        while num > 0:
            if not isprime(num):
                break
            num = num // 10
        if num == 0:
            primes.append(i)
    return sorted(list(set(primes)))