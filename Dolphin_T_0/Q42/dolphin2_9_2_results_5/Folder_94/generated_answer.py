def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    prime_factors = set()
    num = numbers[93]
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            prime_factors.add(i)
    return prime_factors