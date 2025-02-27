def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors_set = set()
    number = numbers[312]
    for i in range(2, number + 1):
        while number % i == 0 and is_prime(i):
            prime_factors_set.add(i)
            number //= i
        if number == 1:
            break
    return prime_factors_set