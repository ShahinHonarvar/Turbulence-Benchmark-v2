def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[46] ** 0.5) + 1):
        if nums[46] % i == 0:
            sum += i + nums[46] // i
    return sum == nums[46]