def find_second_largest_num(numbers):
    if len(numbers) < 31 or len(numbers[20:31]) < 2:
        return None
    slice_numbers = numbers[20:31]
    unique_numbers = list(set(slice_numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]