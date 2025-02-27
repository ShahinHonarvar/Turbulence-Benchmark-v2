def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[63] ** 0.5) + 1):
        if nums[63] % i == 0:
            total += i + nums[63] // i
    return total == nums[63]