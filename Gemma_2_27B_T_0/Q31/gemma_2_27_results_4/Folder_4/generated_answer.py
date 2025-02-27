def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[15] ** 0.5) + 1):
        if nums[15] % i == 0:
            total += i + nums[15] // i
    return total == nums[15]