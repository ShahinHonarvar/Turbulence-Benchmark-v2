def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target = numbers[40]
    factors = set()
    i = 2
    while i * i <= target:
        if target % i:
            i += 1
        else:
            target //= i
            factors.add(i)
    if target > 1:
        factors.add(target)
    prime_factors = set()
    for factor in factors:
        if is_prime(factor):
            prime_factors.add(factor)
    return prime_factors