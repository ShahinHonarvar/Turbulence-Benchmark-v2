def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    slice_of_numbers = numbers[10:11]
    sorted_numbers = sorted(slice_of_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]