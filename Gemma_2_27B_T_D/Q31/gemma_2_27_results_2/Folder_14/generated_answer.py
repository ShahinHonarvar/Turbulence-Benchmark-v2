def if_perfect_num(nums):
    if len(nums) > 17:
        total = 1
        for i in range(2, int(nums[17] ** 0.5) + 1):
            if nums[17] % i == 0:
                total += i + nums[17] // i
        return total == nums[17]
    return False