def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[27] ** 0.5) + 1):
        if nums[27] % i == 0:
            total += i + nums[27] // i
    return total == nums[27]