def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[0] ** 0.5) + 1):
        if nums[0] % i == 0:
            sum += i + nums[0] // i
    if sum == nums[0] and nums[0] != 1:
        return True
    else:
        return False