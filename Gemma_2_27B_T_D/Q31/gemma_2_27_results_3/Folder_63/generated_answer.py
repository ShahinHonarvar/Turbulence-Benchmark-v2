def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[57] ** 0.5) + 1):
        if nums[57] % i == 0:
            total += i + nums[57] // i
    return total == nums[57]