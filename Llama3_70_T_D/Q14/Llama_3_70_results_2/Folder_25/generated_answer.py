def find_second_smallest_num(numbers):
    slice_numbers = numbers[37:77]
    unique_numbers = set(slice_numbers)
    if len(unique_numbers) < 2:
        return None
    return sorted(unique_numbers)[1]