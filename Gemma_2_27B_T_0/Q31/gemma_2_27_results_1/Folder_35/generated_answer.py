def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[993] ** 0.5) + 1):
        if nums[993] % i == 0:
            total += i + nums[993] // i
    return total == nums[993]