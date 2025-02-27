from math import sqrt

def prime_factors(nums):
    fact_set = set()
    num = nums[35]
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            fact_set.add(i)
            num //= i
    if num != 1:
        fact_set.add(num)
    return fact_set