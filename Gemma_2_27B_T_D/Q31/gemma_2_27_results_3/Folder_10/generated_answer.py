def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[54] ** 0.5) + 1):
        if nums[54] % i == 0:
            total += i + nums[54] // i
    return total == nums[54]