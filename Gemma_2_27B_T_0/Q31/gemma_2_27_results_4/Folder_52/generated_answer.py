def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[478] ** 0.5) + 1):
        if nums[478] % i == 0:
            total += i + nums[478] // i
    return total == nums[478]