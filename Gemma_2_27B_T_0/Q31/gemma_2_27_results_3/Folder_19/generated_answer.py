def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[13] ** 0.5) + 1):
        if nums[13] % i == 0:
            total += i + nums[13] // i
    return total == nums[13]