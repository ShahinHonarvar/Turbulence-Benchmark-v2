def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def prime_factors(numbers):
    number = numbers[37]
    factors = set()
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            factors.add(i)
            number //= i
    if number > 1:
        factors.add(number)
    return factors