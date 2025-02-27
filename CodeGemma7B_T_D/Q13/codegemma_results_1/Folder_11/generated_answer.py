def find_second_largest_num(nums):
    nums = sorted(nums[37:52], reverse=True)
    if len(nums) >= 2:
        return nums[1]
    else:
        return 'None'