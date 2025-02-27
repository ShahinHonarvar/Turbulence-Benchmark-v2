def prime_factors(numbers):

    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def prime_factors_of_num(num):
        prime_factors = set()
        for i in range(2, num + 1):
            if is_prime(i) and num % i == 0:
                prime_factors.add(i)
        return prime_factors
    return prime_factors_of_num(numbers[45])