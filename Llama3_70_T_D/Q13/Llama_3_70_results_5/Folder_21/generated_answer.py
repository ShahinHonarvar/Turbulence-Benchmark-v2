def find_second_largest_num(numbers):
    slice_numbers = numbers[639:976]
    slice_numbers.sort(reverse=True)
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]