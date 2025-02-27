def find_second_smallest_num(nums):
    nums = nums[50:201]
    nums.sort()
    if len(nums) > 1:
        return nums[1]
    else:
        return 'None'