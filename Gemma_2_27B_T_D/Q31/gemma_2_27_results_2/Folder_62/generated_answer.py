def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[926] ** 0.5) + 1):
        if nums[926] % i == 0:
            sum += i + nums[926] // i
    return sum == nums[926]