def if_perfect_num(nums):
    if nums[4] == sum((i for i in range(1, nums[4]) if nums[4] % i == 0)):
        return True
    return False