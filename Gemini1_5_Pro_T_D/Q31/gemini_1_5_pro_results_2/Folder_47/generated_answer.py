def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[34] ** 0.5) + 1):
        if nums[34] % i == 0:
            sum += i + nums[34] // i
    if sum == nums[34] and nums[34] != 1:
        return True
    else:
        return False