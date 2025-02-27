def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    num = lst[15]
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0 and isPrime(i):
            factors.add(i)
    return factors