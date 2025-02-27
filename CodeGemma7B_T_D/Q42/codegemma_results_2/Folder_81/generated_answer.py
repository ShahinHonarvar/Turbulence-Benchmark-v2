def prime_factors(nums):
    factors = set()
    num = nums[20]
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num /= i
    if num > 1:
        factors.add(int(num))
    return factors