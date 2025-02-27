def find_second_largest_num(nums):
    nums = nums[74:96]
    nums.sort(reverse=True)
    if len(nums) == 0:
        return 'None'
    return nums[1]