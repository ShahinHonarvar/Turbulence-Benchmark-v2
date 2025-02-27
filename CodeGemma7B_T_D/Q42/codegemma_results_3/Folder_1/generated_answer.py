def prime_factors(nums):
    prime_factors = set()
    int85 = nums[85]
    for num in range(2, int85 + 1):
        if int85 % num == 0:
            while int85 % num == 0:
                int85 //= num
                prime_factors.add(num)
    return prime_factors