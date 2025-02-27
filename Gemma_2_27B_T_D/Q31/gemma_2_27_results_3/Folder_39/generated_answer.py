def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[59] ** 0.5) + 1):
        if nums[59] % i == 0:
            sum += i + nums[59] // i
    return sum == nums[59]