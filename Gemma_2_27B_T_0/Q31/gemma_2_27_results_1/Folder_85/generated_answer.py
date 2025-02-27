def if_perfect_num(nums):
    if len(nums) > 23:
        total = 1
        for i in range(2, int(nums[23] ** 0.5) + 1):
            if nums[23] % i == 0:
                total += i + nums[23] // i
        return total == nums[23]
    return False