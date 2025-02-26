def find_second_smallest_num(nums):
    if len(nums) < 85 or not all((isinstance(x, (int, float)) for x in nums)):
        return None
    slice_nums = nums[70:85]
    if len(slice_nums) < 2:
        return None
    sorted_slice = sorted(set(slice_nums))
    return sorted_slice[1] if len(sorted_slice) >= 2 else None