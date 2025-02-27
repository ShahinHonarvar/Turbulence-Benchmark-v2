def if_perfect_num(nums):
    if nums[41] == sum((i for i in range(1, nums[41]) if nums[41] % i == 0)):
        return True
    else:
        return False