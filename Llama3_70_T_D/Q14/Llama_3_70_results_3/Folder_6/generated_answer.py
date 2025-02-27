def find_second_smallest_num(numbers):
    if 79 < len(numbers):
        slice_numbers = numbers[29:80]
        sorted_numbers = sorted(slice_numbers)
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None