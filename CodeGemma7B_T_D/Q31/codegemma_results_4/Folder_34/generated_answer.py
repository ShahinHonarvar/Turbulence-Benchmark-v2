def if_perfect_num(nums):
    if len(nums) > 97 and nums[97] * nums[97] - sum([i for i in range(1, nums[97]) if nums[97] % i == 0]) == 0:
        return True
    return False