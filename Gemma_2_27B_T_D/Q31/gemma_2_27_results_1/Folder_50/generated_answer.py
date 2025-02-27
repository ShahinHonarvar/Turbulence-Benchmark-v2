def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[40] ** 0.5) + 1):
        if nums[40] % i == 0:
            total += i + nums[40] / i
    return total == nums[40]