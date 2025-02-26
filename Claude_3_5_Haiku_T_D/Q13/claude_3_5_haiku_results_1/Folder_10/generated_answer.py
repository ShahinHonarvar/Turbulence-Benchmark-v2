def find_second_largest_num(numbers):
    if len(numbers) < 27:
        return None
    slice_list = numbers[25:60]
    sorted_slice = sorted(slice_list, reverse=True)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None