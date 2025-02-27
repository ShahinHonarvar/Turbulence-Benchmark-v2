def find_second_largest_num(numbers):
    slice_numbers = numbers[533:606]
    sorted_numbers = sorted(set(slice_numbers), reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]