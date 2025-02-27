def if_perfect_num(nums):
    if sum((i for i in range(1, nums[41]) if nums[41] % i == 0)) == nums[41]:
        return True
    else:
        return False