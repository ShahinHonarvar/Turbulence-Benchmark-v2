def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[8] / 2) + 1):
        if nums[8] % i == 0:
            sum += i
    if sum == nums[8]:
        return True
    else:
        return False