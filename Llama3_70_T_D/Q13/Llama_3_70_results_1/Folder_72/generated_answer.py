def find_second_largest_num(numbers):
    slice_numbers = numbers[29:52]
    sorted_numbers = sorted(set(slice_numbers), reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]