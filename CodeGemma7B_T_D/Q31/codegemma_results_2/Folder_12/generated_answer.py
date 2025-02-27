def if_perfect_num(nums):
    sum = 0
    for i in range(1, nums[27] + 1):
        if nums[27] % i == 0:
            sum += i
    if sum == nums[27]:
        return True
    else:
        return False