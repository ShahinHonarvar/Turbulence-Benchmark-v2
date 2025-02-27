def if_perfect_num(nums):
    if nums[132] % sum(range(1, nums[132])) == 0:
        return True
    else:
        return False