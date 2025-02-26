def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    slice_nums = numbers[25:88]
    if len(slice_nums) < 2:
        return None
    unique_slice_nums = sorted(set(slice_nums), reverse=True)
    if len(unique_slice_nums) < 2:
        return None
    return unique_slice_nums[1]