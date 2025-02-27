def prime_factors(nums):
    prime_factor = set()
    num = nums[92]
    while num > 1:
        for i in range(2, num + 1):
            while num % i == 0:
                prime_factor.add(i)
                num //= i
    return prime_factor