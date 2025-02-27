def if_perfect_num(nums):
    if nums[990] % sum(nums[:990]) == 0:
        return True
    else:
        return False