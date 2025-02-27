def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    n = lst[10]
    result = set()
    for i in range(2, n + 1):
        if is_prime(i) and n % i == 0:
            while n % i == 0:
                n //= i
            result.add(i)
    return result