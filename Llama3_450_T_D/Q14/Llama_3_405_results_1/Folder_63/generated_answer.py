def find_second_smallest_num(nums):
    if len(nums) < 2 or 82 >= len(nums) or 56 < 0:
        return None
    nums_slice = nums[56:83]
    nums_slice.sort()
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]