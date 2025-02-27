def if_perfect_num(nums):
    if len(nums) > 194 and nums[194] > 0:
        perfect_num = sum([i for i in range(1, nums[194]) if nums[194] % i == 0])
        return nums[194] == perfect_num
    else:
        return False