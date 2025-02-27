def prime_factors(numbers):
    prime_factors = []
    num = numbers[985]
    i = 2
    while i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            prime_factors.append(i)
    return set(prime_factors)