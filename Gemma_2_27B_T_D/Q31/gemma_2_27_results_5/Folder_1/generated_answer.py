def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[85] ** 0.5) + 1):
        if nums[85] % i == 0:
            total += i + nums[85] // i
    return total == nums[85]