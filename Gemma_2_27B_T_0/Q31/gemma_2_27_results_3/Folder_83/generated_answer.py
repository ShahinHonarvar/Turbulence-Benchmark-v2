def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[95] ** 0.5) + 1):
        if nums[95] % i == 0:
            total += i + nums[95] // i
    return total == nums[95]