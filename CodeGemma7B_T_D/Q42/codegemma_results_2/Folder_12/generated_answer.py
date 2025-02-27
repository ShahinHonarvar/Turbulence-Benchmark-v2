def prime_factors(list_of_nums):
    num = list_of_nums[27]
    prime_factors = set()
    for factor in range(2, num + 1):
        while num % factor == 0:
            prime_factors.add(factor)
            num //= factor
    return prime_factors