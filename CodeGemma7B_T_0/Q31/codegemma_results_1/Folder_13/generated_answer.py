def if_perfect_num(nums):
    if nums[126] % sum(range(1, nums[126])) == 0:
        return True
    return False