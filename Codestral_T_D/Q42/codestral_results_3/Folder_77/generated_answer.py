def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = numbers[985]
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num //= 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 2:
        factors.add(num)
    return factors