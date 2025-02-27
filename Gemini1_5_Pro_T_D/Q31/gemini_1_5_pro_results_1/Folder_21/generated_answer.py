def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[410] ** 0.5) + 1):
        if nums[410] % i == 0:
            sum += i + nums[410] // i
    if sum == nums[410] and nums[410] != 1:
        return True
    return False