def find_second_smallest_num(numbers):
    if len(numbers) < 558:
        return None
    slice_numbers = numbers[209:557]
    if not slice_numbers:
        return None
    sorted_slice = sorted(slice_numbers)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]