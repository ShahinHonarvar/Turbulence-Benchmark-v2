def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(numbers):
    if len(numbers) < 321:
        return set()
    num = numbers[321]
    factors = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                factors.add(i)
            if i != num // i and is_prime(num // i):
                factors.add(num // i)
    return factors