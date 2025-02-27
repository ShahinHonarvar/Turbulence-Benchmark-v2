def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[40] ** 0.5) + 1):
        if nums[40] % i == 0:
            sum += i + nums[40] // i
    if sum == nums[40] and nums[40] != 1:
        return True
    else:
        return False