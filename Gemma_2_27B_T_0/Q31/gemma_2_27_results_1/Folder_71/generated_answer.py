def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[78] ** 0.5) + 1):
        if nums[78] % i == 0:
            total += i + nums[78] // i
    return total == nums[78]