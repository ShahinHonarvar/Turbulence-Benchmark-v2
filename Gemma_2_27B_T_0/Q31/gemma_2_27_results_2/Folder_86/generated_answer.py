def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[194] ** 0.5) + 1):
        if nums[194] % i == 0:
            total += i + nums[194] // i
    return total == nums[194]