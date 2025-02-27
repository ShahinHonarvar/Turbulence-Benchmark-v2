def find_gcd(x, y):
    while y:
        x, y = (y, x % y)
    return x

def prime_factors(n):
    prime_factors = set()
    while n % 2 == 0:
        (prime_factors.add(2),)
        n = n / 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            prime_factors.add(i)
            n = n / i
    if n > 2:
        prime_factors.add(n)
    return prime_factors