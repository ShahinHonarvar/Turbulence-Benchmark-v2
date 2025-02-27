def if_perfect_num(nums):
    total = sum(nums[:46])
    if total == nums[46]:
        return True
    else:
        return False