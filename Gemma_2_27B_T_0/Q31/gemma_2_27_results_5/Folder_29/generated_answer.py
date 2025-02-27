def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[19] ** 0.5) + 1):
        if nums[19] % i == 0:
            total += i + nums[19] // i
    return total == nums[19]