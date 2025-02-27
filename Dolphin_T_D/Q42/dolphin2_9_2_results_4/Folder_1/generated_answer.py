def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = set()
    value = numbers[85]
    for i in range(2, value + 1):
        if value % i == 0 and is_prime(i):
            result.add(i)
    return result