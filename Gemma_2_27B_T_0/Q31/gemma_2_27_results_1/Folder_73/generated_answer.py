def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[41] ** 0.5) + 1):
        if nums[41] % i == 0:
            total += i + nums[41] // i
    return total == nums[41]