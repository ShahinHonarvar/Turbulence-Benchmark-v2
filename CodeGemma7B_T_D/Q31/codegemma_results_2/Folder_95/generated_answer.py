def if_perfect_num(nums):
    if nums[87] % sum(nums[:87]) == 0:
        return True
    else:
        return False