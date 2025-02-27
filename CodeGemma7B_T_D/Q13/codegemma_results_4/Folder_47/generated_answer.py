def find_second_largest_num(nums):
    if len(nums) < 37 or len(nums) > 76:
        return 'None'
    nums = sorted(nums[37:77], reverse=True)
    return nums[1]