def find_second_largest_num(numbers):
    if len(numbers) < 80:
        return None
    slice_of_numbers = numbers[29:80]
    if len(slice_of_numbers) < 2:
        return None
    unique_numbers = set(slice_of_numbers)
    if len(unique_numbers) < 2:
        return None
    return sorted(unique_numbers)[-2]