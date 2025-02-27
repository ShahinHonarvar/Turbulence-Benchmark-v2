def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    slice_numbers = numbers[22:64]
    sorted_numbers = sorted(set(slice_numbers), reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]