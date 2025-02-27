def prime_factors(numbers):
    return {i for i in {x for x in range(2, numbers[69] + 1) if numbers[69] % x == 0 and is_prime(x)}}

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True