def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    slice_numbers = numbers[75:89]
    sorted_slice = sorted(slice_numbers, reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None