from itertools import combinations_with_replacement
from math import prod

def lists_with_product_equal_n(nums):

    def has_zero_divisors(num):
        divisors = set([1, num])
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)
        return len(divisors) == 2 and 0 in divisors
    for n in nums:
        if has_zero_divisors(n):
            return [[n]]
    products = {}
    for i in range(1, len(nums)):
        for j in range(i):
            products[i - j, j] = prod(nums[j:i])
    result = []
    for (i, j), product in products.items():
        if product == -906:
            sublist = nums[j:i + 1]
            result.append(sublist)
    return result