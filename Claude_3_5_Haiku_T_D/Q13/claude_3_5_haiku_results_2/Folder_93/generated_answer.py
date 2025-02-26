def find_second_largest_num(nums):
    if len(nums) < 96 or len(nums[75:95]) < 2:
        return None
    slice_nums = nums[75:95]
    unique_nums = sorted(set(slice_nums), reverse=True)
    return unique_nums[1] if len(unique_nums) >= 2 else None