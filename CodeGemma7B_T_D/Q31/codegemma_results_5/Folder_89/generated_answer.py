def if_perfect_num(nums):
    return nums[18] % 3 == 0 and nums[18] % 2 == 0 and (nums[18] % 5 == 0) or (nums[18] % 7 == 0 and nums[18] % 5 == 0)