def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[8] ** 0.5) + 1):
        if nums[8] % i == 0:
            total += i + nums[8] // i
    return total == nums[8]