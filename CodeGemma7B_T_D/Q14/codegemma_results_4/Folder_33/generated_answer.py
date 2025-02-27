def find_second_smallest_num(nums):
    if not nums or len(nums) < 263 or max(nums) - min(nums) < 745:
        return None
    nums_slice = sorted(nums[262:747])[1]
    if nums_slice < nums[261]:
        return nums_slice
    else:
        return None