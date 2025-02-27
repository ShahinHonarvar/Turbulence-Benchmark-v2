def is_perfect_num(nums):
    if nums[20] % sum(range(1, nums[20])) == 0:
        return True
    else:
        return False