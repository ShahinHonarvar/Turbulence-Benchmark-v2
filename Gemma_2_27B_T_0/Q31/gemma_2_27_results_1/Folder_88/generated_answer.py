def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[46] ** 0.5) + 1):
        if nums[46] % i == 0:
            total += i + nums[46] // i
    return total == nums[46]