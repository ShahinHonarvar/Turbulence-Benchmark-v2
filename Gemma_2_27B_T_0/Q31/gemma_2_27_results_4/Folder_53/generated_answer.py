def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[73] ** 0.5) + 1):
        if nums[73] % i == 0:
            total += i + nums[73] // i
    return total == nums[73]