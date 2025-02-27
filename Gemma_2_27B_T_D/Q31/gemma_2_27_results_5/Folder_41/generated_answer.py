def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[84] ** 0.5) + 1):
        if nums[84] % i == 0:
            sum += i + nums[84] // i
    return sum == nums[84]