def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[2] ** 0.5) + 1):
        if nums[2] % i == 0:
            total += i + nums[2] // i
    return total == nums[2]