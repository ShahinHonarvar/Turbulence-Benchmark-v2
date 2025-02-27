def if_perfect_num(nums):
    if nums[1] == sum(range(1, nums[1])):
        return True
    else:
        return False