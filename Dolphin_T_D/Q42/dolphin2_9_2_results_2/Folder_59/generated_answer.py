def prime_factors(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_prime_factor(n, factors):
        for i in range(len(factors) - 1, -1, -1):
            if n % factors[i] == 0:
                return factors[i]
        return -1
    third_number = numbers[2]
    factors = set()
    if is_prime(third_number):
        factors.add(third_number)
    else:
        for i in range(3, third_number + 1, 2):
            while third_number % i == 0:
                if third_number % i != i:
                    factors.add(is_prime_factor(third_number, list(factors)))
                else:
                    factors.add(i)
                third_number //= i
    return factors