def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[453] ** 0.5) + 1):
        if nums[453] % i == 0:
            total += i + nums[453] // i
    return total == nums[453]