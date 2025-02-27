def prime_factors(numbers_list):
    if len(numbers_list) <= 74:
        return 'Index Error: The list is not long enough'
    num = numbers_list[74]
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