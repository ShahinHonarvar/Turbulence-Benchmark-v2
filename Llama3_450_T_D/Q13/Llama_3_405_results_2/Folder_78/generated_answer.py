def find_second_largest_num(numbers):
    slice_of_numbers = numbers[43:52]
    if len(slice_of_numbers) < 2:
        return None
    else:
        return sorted(slice_of_numbers)[-2]