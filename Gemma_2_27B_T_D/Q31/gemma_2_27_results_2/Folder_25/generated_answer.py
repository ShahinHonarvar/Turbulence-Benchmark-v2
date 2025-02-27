def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[90] ** 0.5) + 1):
        if nums[90] % i == 0:
            total += i + nums[90] // i
    return total == nums[90]