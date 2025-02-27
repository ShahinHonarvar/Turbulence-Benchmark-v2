def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[92] ** 0.5) + 1):
        if nums[92] % i == 0:
            total += i + nums[92] // i
    return total == nums[92]