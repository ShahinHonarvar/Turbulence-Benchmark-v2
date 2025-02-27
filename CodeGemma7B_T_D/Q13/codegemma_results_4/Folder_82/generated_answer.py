def find_second_largest_num(nums):
    nums = nums[20:201]
    if len(nums) >= 2:
        nums.sort()
        return nums[-2]
    else:
        return 'None'