def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[21] ** 0.5) + 1):
        if nums[21] % i == 0:
            total += i + nums[21] // i
    return total == nums[21]