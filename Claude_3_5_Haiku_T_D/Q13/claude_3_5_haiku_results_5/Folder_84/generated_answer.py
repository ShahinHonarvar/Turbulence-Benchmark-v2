def find_second_largest_num(numbers):
    if len(numbers) <= 43:
        return None
    slice_nums = numbers[43:87]
    if len(slice_nums) < 2:
        return None
    unique_slice_nums = sorted(set(slice_nums), reverse=True)
    return unique_slice_nums[1] if len(unique_slice_nums) >= 2 else None