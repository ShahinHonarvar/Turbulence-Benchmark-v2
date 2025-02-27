def if_perfect_num(nums):
    if nums[247] % sum(range(1, nums[247])) == 0:
        return True
    return False