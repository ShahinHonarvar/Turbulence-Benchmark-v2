def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    slice_numbers = numbers[21:98]
    sorted_numbers = sorted(slice_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]