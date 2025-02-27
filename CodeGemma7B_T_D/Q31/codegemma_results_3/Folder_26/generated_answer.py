def if_perfect_num(nums):
    if nums[222] % sum(range(1, nums[222])) == 0:
        return True
    else:
        return False