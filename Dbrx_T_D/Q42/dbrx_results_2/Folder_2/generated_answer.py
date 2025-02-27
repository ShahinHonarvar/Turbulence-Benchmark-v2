def prime_factors(numbers):
    prime_factors = set()
    num = numbers[702]
    i = 2
    while i <= num:
        if num % i:
            i += 1
        else:
            prime_factors.add(i)
            num //= i
    return prime_factors