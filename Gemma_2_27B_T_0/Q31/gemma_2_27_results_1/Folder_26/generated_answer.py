def if_perfect_num(nums):
    if len(nums) > 222:
        total = 1
        for i in range(2, int(nums[222] ** 0.5) + 1):
            if nums[222] % i == 0:
                total += i + nums[222] // i
        return total == nums[222]
    return False