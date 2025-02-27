def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_factors_set = set()
    number = numbers[828]
    for i in range(2, number + 1):
        if is_prime(i) and number % i == 0:
            prime_factors_set.add(i)
    return prime_factors_set