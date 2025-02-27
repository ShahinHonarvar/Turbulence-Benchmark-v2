def find_second_largest_num(nums):
    nums = nums[28:39]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return 'None'
    else:
        return nums[1]