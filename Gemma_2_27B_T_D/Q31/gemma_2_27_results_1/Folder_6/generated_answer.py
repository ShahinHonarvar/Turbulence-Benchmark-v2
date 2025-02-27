def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[790] ** 0.5) + 1):
        if nums[790] % i == 0:
            total += i + nums[790] // i
    return total == nums[790]