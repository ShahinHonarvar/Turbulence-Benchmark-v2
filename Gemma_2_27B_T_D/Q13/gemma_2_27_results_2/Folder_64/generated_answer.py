def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums_slice = nums[:5]
    nums_slice.sort()
    return nums_slice[-2] if len(nums_slice) > 1 else None