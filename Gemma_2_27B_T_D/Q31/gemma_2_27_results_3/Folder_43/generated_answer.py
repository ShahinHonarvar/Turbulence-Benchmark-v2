def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[29] ** 0.5) + 1):
        if nums[29] % i == 0:
            sum += i + nums[29] // i
    return sum == nums[29]