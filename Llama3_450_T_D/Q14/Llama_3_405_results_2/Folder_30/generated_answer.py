def find_second_smallest_num(numbers):
    if len(numbers) < 53:
        return None
    slice_of_numbers = numbers[26:53]
    if len(slice_of_numbers) < 2:
        return None
    slice_of_numbers.sort()
    return slice_of_numbers[1]