def if_perfect_num(nums):
    if len(nums) > 53:
        total = 1
        for i in range(2, int(nums[53] ** 0.5) + 1):
            if nums[53] % i == 0:
                total += i + nums[53] // i
        return total == nums[53]
    return False