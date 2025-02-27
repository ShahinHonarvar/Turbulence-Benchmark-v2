def find_second_largest_num(numbers):
    slice_numbers = numbers[42:69]
    if len(slice_numbers) < 2:
        return None
    else:
        slice_numbers.sort()
        return slice_numbers[-2]