def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    slice_numbers = numbers[23:24]
    if len(set(slice_numbers)) == 1:
        return None
    sorted_numbers = sorted(slice_numbers)
    return sorted_numbers[1]