def if_perfect_num(nums):
    if len(nums) > 33:
        total = 1
        for i in range(2, int(nums[33] ** 0.5) + 1):
            if nums[33] % i == 0:
                total += i + nums[33] // i
        return total == nums[33]
    return False