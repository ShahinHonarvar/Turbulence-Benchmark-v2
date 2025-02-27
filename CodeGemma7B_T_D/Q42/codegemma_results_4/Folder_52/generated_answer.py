def prime_factors(nums):
    prime_factors = set()
    num = nums[478]
    for i in range(2, num + 1):
        while num % i == 0:
            prime_factors.add(i)
            num //= i
    return prime_factors