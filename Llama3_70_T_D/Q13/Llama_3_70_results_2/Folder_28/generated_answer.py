def find_second_largest_num(numbers):
    slice_numbers = numbers[62:64]
    sorted_slice_numbers = sorted(set(slice_numbers), reverse=True)
    if len(sorted_slice_numbers) < 2:
        return None
    return sorted_slice_numbers[1]