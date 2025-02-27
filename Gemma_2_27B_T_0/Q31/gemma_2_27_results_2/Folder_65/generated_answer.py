def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[35] ** 0.5) + 1):
        if nums[35] % i == 0:
            total += i + nums[35] // i
    return total == nums[35]