def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[49] ** 0.5) + 1):
        if nums[49] % i == 0:
            sum += i + nums[49] / i
    return sum == nums[49]