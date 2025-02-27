def find_second_smallest_num(numbers):
    if len(numbers) < 72:
        return None
    slice_of_numbers = numbers[52:72]
    if len(slice_of_numbers) < 2:
        return None
    return sorted(slice_of_numbers)[1]