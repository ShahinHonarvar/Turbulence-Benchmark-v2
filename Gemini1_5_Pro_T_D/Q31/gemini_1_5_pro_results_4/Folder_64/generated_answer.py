def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[1] / 2) + 1):
        if nums[1] % i == 0:
            sum += i
    if sum == nums[1]:
        return True
    else:
        return False