def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[28] ** 0.5) + 1):
        if nums[28] % i == 0:
            sum += i + nums[28] // i
    if sum == nums[28] and nums[28] != 1:
        return True
    else:
        return False