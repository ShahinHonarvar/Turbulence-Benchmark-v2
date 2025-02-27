def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[48] ** 0.5) + 1):
        if nums[48] % i == 0:
            total += i + nums[48] // i
    return total == nums[48]