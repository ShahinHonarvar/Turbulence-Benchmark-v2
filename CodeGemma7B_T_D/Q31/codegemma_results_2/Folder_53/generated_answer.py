def if_perfect_num(nums):
    if nums[73] % sum(range(1, nums[73])) == 0:
        return True
    return False