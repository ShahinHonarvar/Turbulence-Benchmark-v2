def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[24] ** 0.5) + 1):
        if nums[24] % i == 0:
            total += i + nums[24] // i
    return total == nums[24]