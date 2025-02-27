def prime_factors(nums):
    factorized_num = set(get_factorized_num(nums[33]))
    return factorized_num

def get_factorized_num(num):
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num /= i
    if num > 1:
        factors.add(num)
    return list(factors)