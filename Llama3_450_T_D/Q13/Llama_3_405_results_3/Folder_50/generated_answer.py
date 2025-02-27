def find_second_largest_num(nums):
    if len(nums) < 85:
        return None
    nums_slice = nums[70:85]
    nums_slice.sort(reverse=True)
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]