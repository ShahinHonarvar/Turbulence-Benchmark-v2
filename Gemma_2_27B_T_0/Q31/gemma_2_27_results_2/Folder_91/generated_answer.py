def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[6] ** 0.5) + 1):
        if nums[6] % i == 0:
            total += i + nums[6] // i
    return total == nums[6]