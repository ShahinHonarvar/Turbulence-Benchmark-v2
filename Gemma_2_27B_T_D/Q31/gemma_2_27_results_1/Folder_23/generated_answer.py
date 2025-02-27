def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[69] ** 0.5) + 1):
        if nums[69] % i == 0:
            sum += i + nums[69] // i
    return sum == nums[69]