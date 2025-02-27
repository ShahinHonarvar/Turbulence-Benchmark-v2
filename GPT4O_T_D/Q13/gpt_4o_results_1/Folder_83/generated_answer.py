def find_second_largest_num(numbers):
    if len(numbers) <= 90:
        return None
    slice_numbers = numbers[90:91]
    if len(slice_numbers) <= 1:
        return None
    unique_numbers = list(set(slice_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]