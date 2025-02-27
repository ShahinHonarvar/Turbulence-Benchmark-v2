def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    num = numbers[0]
    while num % 2 == 0:
        factors.add(2)
        num = num // 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num = num // i
    if num > 2:
        factors.add(num)
    return factors