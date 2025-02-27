def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[4] / 2) + 1):
        if nums[4] % i == 0:
            sum += i
    if sum == nums[4]:
        return True
    else:
        return False