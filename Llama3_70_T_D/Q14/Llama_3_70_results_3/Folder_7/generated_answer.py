def find_second_smallest_num(numbers):
    slice_of_numbers = numbers[686:988]
    if len(slice_of_numbers) < 2:
        return None
    return sorted(slice_of_numbers)[1]