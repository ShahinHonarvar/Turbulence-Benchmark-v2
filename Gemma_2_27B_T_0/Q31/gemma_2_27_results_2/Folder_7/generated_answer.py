def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[851] ** 0.5) + 1):
        if nums[851] % i == 0:
            total += i + nums[851] // i
    return total == nums[851]