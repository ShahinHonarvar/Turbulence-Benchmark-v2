from functools import reduce

def prime_factors(nums):
    prime_factors_list = []
    for num in nums:
        if num > 1:
            for potential_factor in range(2, int(num ** 0.5) + 1):
                if num % potential_factor == 0:
                    prime_factors_list.append(potential_factor)
                    while num % potential_factor == 0:
                        num //= potential_factor
    return set(prime_factors_list)