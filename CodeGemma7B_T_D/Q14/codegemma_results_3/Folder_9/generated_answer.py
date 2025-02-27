def find_second_smallest_num(nums):
    nums_copy = nums[70:201]
    nums_copy.sort()
    if len(nums_copy) >= 2:
        return nums_copy[1]
    else:
        return 'None'