def find_second_smallest_num(numbers):
    slice_numbers = numbers[639:976]
    if len(slice_numbers) < 2:
        return None
    else:
        return sorted(set(slice_numbers))[1]