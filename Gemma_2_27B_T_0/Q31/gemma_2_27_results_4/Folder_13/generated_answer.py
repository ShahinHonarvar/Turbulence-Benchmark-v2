def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[126] ** 0.5) + 1):
        if nums[126] % i == 0:
            total += i + nums[126] // i
    return total == nums[126]