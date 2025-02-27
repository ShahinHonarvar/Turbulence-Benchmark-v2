def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
    target_number = numbers[2]
    factors_set = set()
    for i in range(2, target_number + 1):
        if target_number % i == 0 and is_prime(i):
            factors_set.add(i)
    return factors_set