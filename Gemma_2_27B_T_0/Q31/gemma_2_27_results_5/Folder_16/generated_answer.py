def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[162] ** 0.5) + 1):
        if nums[162] % i == 0:
            total += i + nums[162] // i
    return total == nums[162]