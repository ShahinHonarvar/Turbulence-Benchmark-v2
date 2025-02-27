def find_second_largest_num(nums):
    if len(nums) < 60:
        return 'None'
    else:
        return sorted(nums[25:60])[-2]