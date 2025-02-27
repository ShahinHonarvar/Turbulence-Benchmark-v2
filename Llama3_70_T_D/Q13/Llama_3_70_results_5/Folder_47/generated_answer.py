def find_second_largest_num(numbers):
    slice_numbers = numbers[37:77]
    if len(slice_numbers) < 2:
        return None
    return sorted(set(slice_numbers), reverse=True)[1]