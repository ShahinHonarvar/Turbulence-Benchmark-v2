def if_perfect_num(nums):
    if len(nums) > 87 and sum([i for i in range(1, nums[87]) if nums[87] % i == 0]) == nums[87]:
        return True
    return False