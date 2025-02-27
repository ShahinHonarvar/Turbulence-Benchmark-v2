def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[4] ** 0.5) + 1):
        if nums[4] % i == 0:
            sum += i + nums[4] / i
    return sum == nums[4]