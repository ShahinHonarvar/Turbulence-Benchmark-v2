def if_perfect_num(nums):
    if len(nums) > 35 and nums[35] == sum([i for i in range(1, nums[35]) if nums[35] % i == 0]):
        return True
    else:
        return False