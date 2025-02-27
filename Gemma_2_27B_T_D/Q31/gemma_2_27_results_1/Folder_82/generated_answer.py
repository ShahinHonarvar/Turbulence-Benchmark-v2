def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[83] ** 0.5) + 1):
        if nums[83] % i == 0:
            total += i + nums[83] // i
    return total == nums[83]