def if_perfect_num(nums):
    if nums[276] % sum(range(1, nums[276])) == 0:
        return True
    return False