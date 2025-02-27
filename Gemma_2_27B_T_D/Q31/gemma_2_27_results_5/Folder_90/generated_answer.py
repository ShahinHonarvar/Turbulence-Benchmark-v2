def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[263] ** 0.5) + 1):
        if nums[263] % i == 0:
            sum += i + nums[263] // i
    return sum == nums[263]