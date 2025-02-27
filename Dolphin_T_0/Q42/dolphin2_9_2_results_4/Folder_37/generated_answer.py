def prime_factors():

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_for_number(n):
        factors = set()
        for i in range(2, n + 1):
            if is_prime(i) and n % i == 0:
                factors.add(i)
        return factors
    numbers = [1, 5, 8, 10, 13, 21, 35, 42, 45, 65, 70, 78, 84, 105, 120, 135, 140, 150, 160, 180, 210, 215, 220, 225, 240, 255, 270, 285, 420, 315, 350, 525, 600, 850, 1050, 1250, 5000, 10000, 50000, 100000, 500000, 1000000, 10000000]
    return prime_factors_for_number(numbers[28])