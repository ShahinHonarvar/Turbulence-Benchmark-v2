def if_perfect_num(nums):
    if len(nums) > 478 and nums[478] == sum(list(filter(lambda x: nums[478] % x == 0, range(1, nums[478])))):
        return True
    else:
        return False