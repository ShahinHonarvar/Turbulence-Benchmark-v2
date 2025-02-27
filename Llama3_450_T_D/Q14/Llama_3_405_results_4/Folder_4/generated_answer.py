def find_second_smallest_num(nums):
    slice = nums[70:85]
    if len(slice) < 2:
        return None
    else:
        slice.sort()
        return slice[1]