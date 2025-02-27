def if_perfect_num(nums):
    if len(nums) > 43:
        total = 1
        for i in range(2, int(nums[43] ** 0.5) + 1):
            if nums[43] % i == 0:
                total += i + nums[43] // i
        return total == nums[43]
    else:
        return False