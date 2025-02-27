def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[80] ** 0.5) + 1):
        if nums[80] % i == 0:
            total += i + nums[80] // i
    return total == nums[80]