def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    num = numbers[43]
    factors = set()
    i = 2
    while i <= num:
        if is_prime(i) and num % i == 0:
            factors.add(i)
            num = num / i
        else:
            i += 1
    return factors