def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[312] ** 0.5) + 1):
        if nums[312] % i == 0:
            total += i + nums[312] // i
    return total == nums[312]