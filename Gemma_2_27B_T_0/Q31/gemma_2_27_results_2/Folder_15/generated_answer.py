def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[10] ** 0.5) + 1):
        if nums[10] % i == 0:
            total += i + nums[10] // i
    return total == nums[10]