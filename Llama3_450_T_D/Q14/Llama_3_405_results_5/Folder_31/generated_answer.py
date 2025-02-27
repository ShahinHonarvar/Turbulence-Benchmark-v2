def find_second_smallest_num(numbers):
    slice_numbers = numbers[29:94]
    if len(slice_numbers) < 2:
        return None
    return sorted(slice_numbers)[1]