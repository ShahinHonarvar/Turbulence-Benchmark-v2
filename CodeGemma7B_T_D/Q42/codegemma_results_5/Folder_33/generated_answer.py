def prime_factors(numbers):
    return {factor for number in numbers for factor in range(2, number + 1) if number % factor == 0 and number != factor and prime(factor)}

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True