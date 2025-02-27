def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[733] ** 0.5) + 1):
        if nums[733] % i == 0:
            total += i + nums[733] // i
    return total == nums[733]