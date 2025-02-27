def if_perfect_num(nums):
    if nums and sum((i for i in range(1, nums[0]) if nums[0] % i == 0)) == nums[0]:
        return True
    return False