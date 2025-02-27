def find_second_smallest_num(numbers):
    slice_numbers = numbers[26:53]
    sorted_unique_numbers = sorted(set(slice_numbers))
    if len(sorted_unique_numbers) < 2:
        return None
    return sorted_unique_numbers[1]