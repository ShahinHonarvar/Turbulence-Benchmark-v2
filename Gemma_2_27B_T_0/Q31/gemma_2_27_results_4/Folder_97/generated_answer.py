def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[132] ** 0.5) + 1):
        if nums[132] % i == 0:
            total += i + nums[132] // i
    return total == nums[132]