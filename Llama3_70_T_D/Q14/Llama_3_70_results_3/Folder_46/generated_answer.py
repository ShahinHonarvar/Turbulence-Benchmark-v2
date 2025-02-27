def find_second_smallest_num(numbers):
    slice_numbers = numbers[13:69]
    if len(slice_numbers) < 2:
        return None
    slice_numbers.sort()
    return slice_numbers[1]