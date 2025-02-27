def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[849] ** 0.5) + 1):
        if nums[849] % i == 0:
            total += i + nums[849] // i
    return total == nums[849]