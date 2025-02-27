def prime_factors(nums):
    return set((prime_factor(nums[88]) for num in nums))

def prime_factor(num):
    result = set()
    divisor = 2
    while divisor ** 2 <= num:
        while num % divisor == 0:
            result.add(divisor)
            num //= divisor
        divisor += 1
    if num > 1:
        result.add(num)
    return result