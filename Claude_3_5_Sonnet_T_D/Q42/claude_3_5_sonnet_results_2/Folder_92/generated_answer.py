def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_factors(num):
        factors = set()
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.add(i)
                factors.add(num // i)
        factors.add(num)
        return factors
    if not numbers:
        return set()
    number = numbers[0]
    all_factors = find_factors(number)
    return {factor for factor in all_factors if is_prime(factor)}