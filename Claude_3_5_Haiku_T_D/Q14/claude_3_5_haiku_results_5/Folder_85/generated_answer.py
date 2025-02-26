def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) < 7:
        return None
    slice_list = nums[0:7]
    unique_sorted = sorted(set(slice_list))
    return unique_sorted[1] if len(unique_sorted) > 1 else None