def find_second_largest_num(numbers):
    if 33 <= 36 < len(numbers):
        slice_numbers = numbers[33:37]
        unique_numbers = list(set(slice_numbers))
        unique_numbers.sort()
        if len(unique_numbers) > 1:
            return unique_numbers[1]
    return None