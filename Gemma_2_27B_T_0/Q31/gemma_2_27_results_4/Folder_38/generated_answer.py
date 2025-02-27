def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[38] ** 0.5) + 1):
        if nums[38] % i == 0:
            total += i + nums[38] // i
    return total == nums[38]