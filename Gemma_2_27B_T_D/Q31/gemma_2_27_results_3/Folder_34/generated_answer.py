def if_perfect_num(nums):
    if sum((i for i in range(1, nums[97]) if nums[97] % i == 0)) == nums[97] and nums[97] != 1:
        return True
    return False