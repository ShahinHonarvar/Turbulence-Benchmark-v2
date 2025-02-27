def if_perfect_num(nums):
    if nums[13] % sum((i for i in range(1, nums[13]) if i % nums[13] == 0)) == 0:
        return True
    else:
        return False