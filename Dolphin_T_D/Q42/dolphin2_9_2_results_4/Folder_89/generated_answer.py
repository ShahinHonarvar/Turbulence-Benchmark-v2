def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    prime_factors_set = set()
    for factor in range(2, numbers[18] + 1):
        while numbers[18] % factor == 0:
            if is_prime(factor):
                prime_factors_set.add(factor)
            numbers[18] //= factor
    return prime_factors_set