def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[746] ** 0.5) + 1):
        if nums[746] % i == 0:
            total += i + nums[746] // i
    return total == nums[746]