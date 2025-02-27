def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    number = numbers[849]
    factors = set()
    i = 2
    while i * i <= number:
        if number % i == 0:
            if is_prime(i):
                factors.add(i)
            number = number / i
        else:
            i += 1
    if number > 1:
        if is_prime(number):
            factors.add(int(number))
    return factors