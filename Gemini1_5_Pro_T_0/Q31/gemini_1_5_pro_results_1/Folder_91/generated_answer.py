def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[6] ** 0.5) + 1):
        if nums[6] % i == 0:
            sum += i + nums[6] // i
    if sum == nums[6] and nums[6] != 1:
        return True
    else:
        return False