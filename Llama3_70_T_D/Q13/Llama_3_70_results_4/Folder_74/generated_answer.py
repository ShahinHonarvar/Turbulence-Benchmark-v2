def find_second_largest_num(numbers):
    if len(numbers) < 79:
        return None
    slice_numbers = numbers[17:79]
    if len(set(slice_numbers)) < 2:
        return None
    return sorted(set(slice_numbers))[-2]