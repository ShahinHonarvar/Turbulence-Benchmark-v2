def prime_factors(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    numbers = numbers[985]
    factors = set()
    i = 2
    while i * i <= numbers:
        if numbers % i:
            i += 1
        else:
            numbers //= i
            if is_prime(i):
                factors.add(i)
    if numbers > 1:
        if is_prime(numbers):
            factors.add(numbers)
    return factors