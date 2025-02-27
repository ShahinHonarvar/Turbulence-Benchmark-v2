def prime_factors(nums):
    """Returns the set of all prime factors of the integer at index 92 in the list 'nums'."""
    factor = []
    num = nums[92]
    for i in range(2, num):
        while num % i == 0:
            factor.append(i)
            num = num / i
    if num > 1:
        factor.append(num)
    return set(factor)