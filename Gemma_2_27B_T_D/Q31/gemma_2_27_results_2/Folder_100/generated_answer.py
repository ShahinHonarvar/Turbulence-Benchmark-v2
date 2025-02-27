def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[99] ** 0.5) + 1):
        if nums[99] % i == 0:
            total += i + nums[99] / i
    return total == nums[99]