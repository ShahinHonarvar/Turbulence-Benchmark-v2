def if_perfect_num(nums):
    if len(nums) > 34:
        total = 1
        for i in range(2, int(nums[34] ** 0.5) + 1):
            if nums[34] % i == 0:
                total += i + nums[34] // i
        return total == nums[34]
    else:
        return False