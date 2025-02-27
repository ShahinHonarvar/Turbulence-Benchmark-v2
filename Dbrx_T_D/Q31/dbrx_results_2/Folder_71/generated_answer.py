def if_perfect_num(nums):
    if len(nums) > 78 and nums[78] == sum([i for i in range(1, nums[78]) if nums[78] % i == 0]):
        return True
    else:
        return False