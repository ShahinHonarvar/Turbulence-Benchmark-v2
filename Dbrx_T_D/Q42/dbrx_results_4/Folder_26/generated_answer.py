def prime_factors(numbers):
    prime_factors = set()
    num = numbers[222]
    i = 2
    while i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            prime_factors.add(i)
    return prime_factors