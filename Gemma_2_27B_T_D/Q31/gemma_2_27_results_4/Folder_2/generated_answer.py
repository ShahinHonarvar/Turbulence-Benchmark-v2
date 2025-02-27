def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[702] ** 0.5) + 1):
        if nums[702] % i == 0:
            total += i + nums[702] // i
    return total == nums[702]