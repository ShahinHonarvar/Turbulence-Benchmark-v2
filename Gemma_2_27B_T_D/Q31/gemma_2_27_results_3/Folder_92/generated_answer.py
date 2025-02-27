def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[0] ** 0.5) + 1):
        if nums[0] % i == 0:
            total += i + nums[0] // i
    return total == nums[0]