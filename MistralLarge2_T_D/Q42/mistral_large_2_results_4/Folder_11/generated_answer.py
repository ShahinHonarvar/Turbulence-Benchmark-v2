def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    num = numbers[77]
    factors = set()
    for i in range(2, num + 1):
        while num % i == 0:
            if is_prime(i):
                factors.add(i)
            num //= i
    return factors