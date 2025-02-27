def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[87] ** 0.5) + 1):
        if nums[87] % i == 0:
            total += i + nums[87] / i
    return total == nums[87]