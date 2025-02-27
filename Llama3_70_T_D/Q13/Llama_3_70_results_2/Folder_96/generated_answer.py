def find_second_largest_num(numbers):
    slice_numbers = numbers[15:52]
    if len(slice_numbers) < 2:
        return None
    else:
        return sorted(set(slice_numbers), reverse=True)[1]