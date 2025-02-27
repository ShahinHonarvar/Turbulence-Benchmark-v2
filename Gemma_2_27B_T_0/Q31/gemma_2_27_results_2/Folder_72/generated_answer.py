def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[16] ** 0.5) + 1):
        if nums[16] % i == 0:
            total += i + nums[16] // i
    return total == nums[16]