def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[53] ** 0.5) + 1):
        if nums[53] % i == 0:
            sum += i + nums[53] // i
    return sum == nums[53]