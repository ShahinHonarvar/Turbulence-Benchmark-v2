def find_second_largest_num(numbers):
    slice_numbers = sorted(numbers[32:36], reverse=True)
    if len(slice_numbers) > 1:
        return slice_numbers[1]
    else:
        return None