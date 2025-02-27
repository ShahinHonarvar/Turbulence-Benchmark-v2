def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    slice_of_numbers = numbers[6:7]
    if len(slice_of_numbers) < 2:
        return None
    return sorted(slice_of_numbers)[1]