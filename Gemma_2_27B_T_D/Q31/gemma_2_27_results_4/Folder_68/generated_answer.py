def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[3] ** 0.5) + 1):
        if nums[3] % i == 0:
            total += i + nums[3] // i
    return total == nums[3]