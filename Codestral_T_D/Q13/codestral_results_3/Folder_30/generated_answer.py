def find_second_largest_num(numbers):
    slice_numbers = numbers[55:99]
    if len(slice_numbers) < 2:
        return None
    else:
        slice_numbers.sort()
        return slice_numbers[-2]