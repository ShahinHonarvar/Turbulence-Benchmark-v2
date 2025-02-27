def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[84] ** 0.5) + 1):
        if nums[84] % i == 0:
            total += i + nums[84] // i
    return total == nums[84]