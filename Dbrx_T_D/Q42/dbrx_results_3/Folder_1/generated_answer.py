def prime_factors(numbers):
    return {factor for num in numbers[numbers[85] == num] for factor in factors(num) if is_prime(factor)}

def factors(n):
    return {i for i in range(1, n + 1) if n % i == 0}

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True