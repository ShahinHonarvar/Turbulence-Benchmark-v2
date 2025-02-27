def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[845] ** 0.5) + 1):
        if nums[845] % i == 0:
            total += i + nums[845] // i
    return total == nums[845]