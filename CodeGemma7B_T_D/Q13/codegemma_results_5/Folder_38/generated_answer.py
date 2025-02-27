def find_second_largest_num(nums):
    nums = sorted(nums[22:64])
    if len(nums) < 2:
        return 'None'
    else:
        return nums[-2]