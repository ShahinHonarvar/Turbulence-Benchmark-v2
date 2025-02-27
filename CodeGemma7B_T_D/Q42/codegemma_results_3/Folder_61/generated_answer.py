import math

def prime_factors(nums):
    prime_factors = set()
    num = nums[8]
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            prime_factors.add(i)
            num //= i
    if num > 1:
        prime_factors.add(num)
    return prime_factors