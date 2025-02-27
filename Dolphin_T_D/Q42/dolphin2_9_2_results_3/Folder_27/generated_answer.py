def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(numbers):
    return set((i for i in range(2, numbers[56]) if is_prime(i) and numbers[56] % i == 0))