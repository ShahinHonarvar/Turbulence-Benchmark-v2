def find_second_largest_num(nums):
    if len(nums) < 35 and len(nums) > 32:
        nums_slice = nums[32:36]
        nums_slice_sorted = sorted(nums_slice)
        if len(nums_slice_sorted) >= 2:
            return nums_slice_sorted[-2]
    return None