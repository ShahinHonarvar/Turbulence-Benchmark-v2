def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[73] ** 0.5) + 1):
        if nums[73] % i == 0:
            sum += i + nums[73] // i
    return sum == nums[73]