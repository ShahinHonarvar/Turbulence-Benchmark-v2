def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    slice_numbers = numbers[50:55]
    sorted_numbers = sorted(slice_numbers, reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]