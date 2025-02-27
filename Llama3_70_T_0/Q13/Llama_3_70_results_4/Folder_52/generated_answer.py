def find_second_largest_num(numbers):
    if len(numbers) < 39:
        return None
    slice_numbers = numbers[28:39]
    slice_numbers.sort(reverse=True)
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]