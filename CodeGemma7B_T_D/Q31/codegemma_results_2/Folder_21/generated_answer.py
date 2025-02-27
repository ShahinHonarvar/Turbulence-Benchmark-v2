def if_perfect_num(nums):
    x = 0
    sum = 0
    for i in range(len(nums)):
        if i == 410:
            x = nums[410]
    for j in range(1, x):
        if x % j == 0:
            sum += j
    if sum == x:
        return True
    else:
        return False