def if_perfect_num(nums):
    if nums[19] % sum(range(1, nums[19])) == 0:
        return True
    else:
        return False