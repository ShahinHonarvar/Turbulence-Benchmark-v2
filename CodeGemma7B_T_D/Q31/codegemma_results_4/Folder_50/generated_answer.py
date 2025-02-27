def if_perfect_num(nums):
    if nums[40] % sum([num for num in nums[:40]]) == 0:
        return True
    return False