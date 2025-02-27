def find_second_smallest_num(nums):
    if len(nums[12:93]) < 2:
        return 'None'
    else:
        return sorted(nums[12:93])[1]