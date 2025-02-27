def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[93] ** 0.5) + 1):
        if nums[93] % i == 0:
            total += i + nums[93] // i
    return total == nums[93]