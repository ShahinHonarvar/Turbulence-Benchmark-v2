def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    if len(numbers) <= 993:
        return set()
    number = numbers[993]
    factors = set()
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            if is_prime(i):
                factors.add(i)
            number //= i
    if number > 1 and is_prime(number):
        factors.add(number)
    return factors