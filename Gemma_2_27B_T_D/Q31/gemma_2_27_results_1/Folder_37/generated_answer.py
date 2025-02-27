def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[28] ** 0.5) + 1):
        if nums[28] % i == 0:
            sum += i + nums[28] // i
    return sum == nums[28]