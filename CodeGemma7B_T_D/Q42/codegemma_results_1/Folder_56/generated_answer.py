def prime_factors(numbers):
    primenumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    factorset = set()
    if len(numbers) > 60:
        num = numbers[60]
    else:
        num = -1
    for p in primenumbers:
        if num % p == 0:
            factorset.add(p)
            while num % p == 0:
                num = num // p
    if num > 1:
        factorset.add(num)
    return factorset