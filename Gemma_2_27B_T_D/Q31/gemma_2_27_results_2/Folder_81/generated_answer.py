def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[20] ** 0.5) + 1):
        if nums[20] % i == 0:
            total += i + nums[20] // i
    return total == nums[20]