def prime_factors(numbers):
    prime_factors = set()
    number = numbers[87]
    i = 2
    while i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            prime_factors.add(i)
    return prime_factors