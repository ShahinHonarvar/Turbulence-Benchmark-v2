def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    slice_of_numbers = numbers[10:11]
    if len(slice_of_numbers) < 2:
        return None
    return sorted(slice_of_numbers)[1]