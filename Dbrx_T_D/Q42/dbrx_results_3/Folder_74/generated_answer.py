def prime_factors(numbers):
    result = set()
    num = numbers[48]
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            result.add(i)
    if num > 1:
        result.add(num)
    return result