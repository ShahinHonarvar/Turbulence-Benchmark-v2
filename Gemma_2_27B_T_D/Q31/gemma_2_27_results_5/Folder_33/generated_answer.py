def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[321] ** 0.5) + 1):
        if nums[321] % i == 0:
            sum += i + nums[321] // i
    return sum == nums[321]