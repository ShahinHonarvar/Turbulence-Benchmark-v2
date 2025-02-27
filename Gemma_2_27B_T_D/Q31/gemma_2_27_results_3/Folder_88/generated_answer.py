def if_perfect_num(nums):
    if sum((i for i in range(1, nums[46]) if nums[46] % i == 0)) == nums[46]:
        return True
    return False