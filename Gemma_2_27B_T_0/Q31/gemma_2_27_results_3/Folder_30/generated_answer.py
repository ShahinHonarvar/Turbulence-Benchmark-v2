def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[94] ** 0.5) + 1):
        if nums[94] % i == 0:
            total += i + nums[94] // i
    return total == nums[94]