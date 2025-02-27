def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[132] ** 0.5) + 1):
        if nums[132] % i == 0:
            sum += i + nums[132] // i
    return sum == nums[132]