def find_second_smallest_num(nums):
    nums_slice = nums[66:94]
    if not nums_slice:
        return 'None'
    else:
        return sorted(nums_slice)[1]