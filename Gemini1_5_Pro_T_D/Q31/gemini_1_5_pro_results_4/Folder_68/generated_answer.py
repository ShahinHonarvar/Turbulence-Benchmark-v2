def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[3] ** 0.5) + 1):
        if nums[3] % i == 0:
            sum += i + nums[3] // i
    if sum == nums[3] and nums[3] != 1:
        return True
    else:
        return False