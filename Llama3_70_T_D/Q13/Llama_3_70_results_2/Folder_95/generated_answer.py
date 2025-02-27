def find_second_largest_num(numbers):
    if len(numbers) > 86:
        slice_numbers = sorted(numbers[82:87])
        return slice_numbers[-2] if len(slice_numbers) > 1 else None
    else:
        return None