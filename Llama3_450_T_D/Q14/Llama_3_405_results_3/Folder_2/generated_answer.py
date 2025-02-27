def find_second_smallest_num(numbers):
    slice_numbers = numbers[43:87]
    sorted_numbers = sorted(slice_numbers)
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]