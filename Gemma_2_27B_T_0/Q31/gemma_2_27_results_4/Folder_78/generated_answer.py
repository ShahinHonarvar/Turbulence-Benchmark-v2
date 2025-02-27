def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[91] ** 0.5) + 1):
        if nums[91] % i == 0:
            total += i + nums[91] // i
    return total == nums[91]