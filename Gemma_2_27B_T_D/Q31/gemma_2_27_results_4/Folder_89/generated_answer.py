def if_perfect_num(nums):
    if sum((i for i in range(1, nums[18]) if nums[18] % i == 0)) == nums[18]:
        return True
    return False