def if_perfect_num(nums):
    if len(nums) > 45:
        if sum((1 for i in range(1, nums[45]))) == nums[45]:
            return True
    return False