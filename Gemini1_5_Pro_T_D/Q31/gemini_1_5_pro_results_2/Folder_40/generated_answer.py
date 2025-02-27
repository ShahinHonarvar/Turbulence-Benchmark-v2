def if_perfect_num(nums):
    sum = 1
    for i in range(2, int(nums[7] / 2) + 1):
        if nums[7] % i == 0:
            sum += i
    if sum == nums[7]:
        return True
    else:
        return False