def prime_factors(numbers):
    return {factor for number in numbers[45:] for factor in {n for n in range(2, number) if number % n == 0} if is_prime(factor)}

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True