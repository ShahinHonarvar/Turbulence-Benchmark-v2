def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors_set = set()
    number = numbers[93]
    i = 2
    while i * i <= number:
        if number % i == 0:
            if is_prime(i):
                prime_factors_set.add(i)
            if is_prime(number // i):
                prime_factors_set.add(number // i)
        i += 1
    return prime_factors_set