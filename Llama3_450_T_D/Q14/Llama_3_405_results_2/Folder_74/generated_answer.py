def find_second_smallest_num(nums):
    if len(nums) < 2 or 46 >= len(nums) or 36 < 0:
        return None
    nums_slice = nums[36:47]
    if len(nums_slice) < 2:
        return None
    nums_slice.sort()
    return nums_slice[1]