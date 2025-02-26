def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    if len(numbers) <= 985:
        return set()
    target = numbers[985]
    factors = set()
    for i in range(2, int(target ** 0.5) + 1):
        while target % i == 0:
            if is_prime(i):
                factors.add(i)
            target //= i
    if target > 1 and is_prime(target):
        factors.add(target)
    return factors