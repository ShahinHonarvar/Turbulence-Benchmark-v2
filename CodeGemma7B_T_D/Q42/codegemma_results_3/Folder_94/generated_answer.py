def prime_factors(nums):
    prime_factors = set()
    for num in nums[93]:
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                prime_factors.add(i)
                num //= i
    return prime_factors