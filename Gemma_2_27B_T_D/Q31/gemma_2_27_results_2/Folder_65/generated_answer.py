def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[35] ** 0.5) + 1):
        if nums[35] % i == 0:
            sum = sum + i + nums[35] // i
    return sum == nums[35]