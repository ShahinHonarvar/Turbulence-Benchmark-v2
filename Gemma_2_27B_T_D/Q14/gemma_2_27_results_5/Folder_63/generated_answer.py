def find_second_smallest_num(nums):
    nums_slice = nums[56:83]
    if len(nums_slice) < 2:
        return None
    return sorted(nums_slice)[1]