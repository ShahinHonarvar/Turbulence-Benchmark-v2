def if_perfect_num(nums):
    if nums[276] <= 1:
        return False
    sum1 = 1
    for i in range(2, int(nums[276] ** 0.5) + 1):
        if nums[276] % i == 0:
            sum1 += i + nums[276] // i
    return sum1 == nums[276]