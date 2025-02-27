def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(lst):
    num = lst[478]
    factors = set()
    i = 2
    while i <= num:
        if num % i == 0 and is_prime(i):
            factors.add(i)
        i += 1
    return factors