def find_second_largest_num(numbers):
    if len(numbers) < 23:
        return None
    slice_nums = numbers[22:51]
    if len(slice_nums) == 0:
        return None
    sorted_slice = sorted(set(slice_nums), reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None