def if_perfect_num(nums):
    if nums[162] % sum(range(1, nums[162])) == 0:
        return True
    else:
        return False