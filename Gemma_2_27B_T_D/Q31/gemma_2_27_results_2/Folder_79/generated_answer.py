def if_perfect_num(nums):
    if sum((i for i in range(1, nums[63]))) == nums[63]:
        return True
    else:
        return False