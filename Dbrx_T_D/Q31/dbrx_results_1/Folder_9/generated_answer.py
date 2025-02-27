def if_perfect_num(nums):
    if len(nums) > 24 and nums[24] == sum([i for i in range(1, nums[24]) if nums[24] % i == 0]):
        return True
    else:
        return False