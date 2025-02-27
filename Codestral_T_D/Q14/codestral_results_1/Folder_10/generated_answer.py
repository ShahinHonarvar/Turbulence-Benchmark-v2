def find_second_smallest_num(nums):
    if 62 <= len(nums) <= 92:
        slice_nums = sorted(nums[62:93])
        return slice_nums[1] if len(slice_nums) > 1 else None
    return None