def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[276] ** 0.5) + 1):
        if nums[276] % i == 0:
            total += i + nums[276] // i
    return total == nums[276]