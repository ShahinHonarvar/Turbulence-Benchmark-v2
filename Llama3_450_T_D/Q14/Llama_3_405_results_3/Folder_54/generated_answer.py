def find_second_smallest_num(numbers):
    slice_of_numbers = numbers[68:87]
    if len(slice_of_numbers) < 2:
        return None
    else:
        return sorted(slice_of_numbers)[1]