def prime_factors(numbers):
    if 990 not in range(len(numbers)):
        return set()
    num = numbers[990]
    i = 2
    factors = set()
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
    if num > 1:
        factors.add(num)
    return factors