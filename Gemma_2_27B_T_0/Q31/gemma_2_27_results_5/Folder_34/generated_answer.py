def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[97] ** 0.5) + 1):
        if nums[97] % i == 0:
            total += i + nums[97] // i
    return total == nums[97]