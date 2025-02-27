def find_second_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    slice_numbers = numbers[15:40]
    sorted_numbers = sorted(set(slice_numbers))
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]