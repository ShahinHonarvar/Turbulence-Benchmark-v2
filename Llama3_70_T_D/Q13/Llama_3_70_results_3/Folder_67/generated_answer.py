def find_second_largest_num(nums):
    slice = nums[22:51]
    if len(slice) < 2:
        return None
    slice.remove(max(slice))
    return max(slice)