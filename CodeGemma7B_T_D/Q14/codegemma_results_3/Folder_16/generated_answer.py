def find_second_smallest_num(nums):
    nums = sorted(nums[66:78])
    if len(nums) < 2:
        return 'None'
    else:
        return nums[1]