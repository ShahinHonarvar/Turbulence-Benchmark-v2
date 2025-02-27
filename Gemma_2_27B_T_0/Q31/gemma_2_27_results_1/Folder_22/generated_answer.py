def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[72] ** 0.5) + 1):
        if nums[72] % i == 0:
            total += i + nums[72] // i
    return total == nums[72]