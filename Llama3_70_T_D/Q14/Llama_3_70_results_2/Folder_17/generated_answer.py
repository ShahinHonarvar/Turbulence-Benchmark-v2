def find_second_smallest_num(numbers):
    if len(numbers) < 39 or not all((isinstance(x, (int, float)) for x in numbers)):
        return None
    slice_of_numbers = numbers[28:39]
    sorted_slice = sorted(slice_of_numbers)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]