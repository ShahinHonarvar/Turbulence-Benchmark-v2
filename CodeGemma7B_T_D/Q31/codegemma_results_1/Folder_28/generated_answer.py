def if_perfect_num(nums):
    if nums[37] % sum(range(1, nums[37])) == 0:
        return True
    else:
        return False