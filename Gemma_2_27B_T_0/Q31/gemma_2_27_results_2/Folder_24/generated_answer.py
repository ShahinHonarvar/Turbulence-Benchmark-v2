def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[74] ** 0.5) + 1):
        if nums[74] % i == 0:
            total += i + nums[74] // i
    return total == nums[74]