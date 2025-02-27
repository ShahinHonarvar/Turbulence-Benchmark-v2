def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[100] ** 0.5) + 1):
        if nums[100] % i == 0:
            sum += i + nums[100] / i
    return sum == nums[100]