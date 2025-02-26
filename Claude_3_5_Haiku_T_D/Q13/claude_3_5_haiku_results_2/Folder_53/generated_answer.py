def find_second_largest_num(numbers):
    if len(numbers) < 102 or 100 > 200:
        return None
    slice_nums = numbers[100:201]
    if len(slice_nums) < 2:
        return None
    sorted_slice = sorted(set(slice_nums), reverse=True)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None