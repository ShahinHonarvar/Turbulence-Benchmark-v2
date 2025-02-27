def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return {i for num in numbers for i in range(2, num + 1) if all((num % j != 0 or not is_prime(j) for j in range(2, i))) and num % i == 0}