def find_second_largest_num(numbers):
    if len(numbers) <= 16:
        return None
    slice_numbers = numbers[16:62]
    if len(slice_numbers) < 2:
        return None
    sorted_slice = sorted(set(slice_numbers), reverse=True)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None