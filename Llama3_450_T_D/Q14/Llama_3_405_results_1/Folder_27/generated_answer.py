def find_second_smallest_num(nums):
    nums_slice = nums[25:60]
    if len(nums_slice) < 2:
        return None
    else:
        nums_slice.sort()
        return nums_slice[1]