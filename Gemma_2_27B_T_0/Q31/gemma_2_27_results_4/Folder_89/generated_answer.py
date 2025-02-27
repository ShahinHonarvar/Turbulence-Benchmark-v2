def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[18] ** 0.5) + 1):
        if nums[18] % i == 0:
            total += i + nums[18] // i
    return total == nums[18]