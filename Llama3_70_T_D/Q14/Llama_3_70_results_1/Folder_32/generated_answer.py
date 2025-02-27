def find_second_smallest_num(nums):
    if len(nums) < 36:
        return None
    nums_slice = sorted(nums[32:36])
    return nums_slice[1] if len(nums_slice) > 1 else None