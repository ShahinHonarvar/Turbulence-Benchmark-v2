def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[24] ** 0.5) + 1):
        if nums[24] % i == 0:
            sum = sum + i + nums[24] // i
    return sum == nums[24]