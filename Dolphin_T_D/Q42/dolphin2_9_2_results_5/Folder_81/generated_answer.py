def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_set = set()
    number = numbers[20]
    for i in range(2, number + 1):
        if is_prime(i) and number % i == 0:
            prime_set.add(i)
    return prime_set