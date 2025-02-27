def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[1] ** 0.5) + 1):
        if nums[1] % i == 0:
            total += i + nums[1] // i
    return total == nums[1]