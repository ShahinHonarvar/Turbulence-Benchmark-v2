def find_second_largest_num(numbers):
    if len(numbers) < 77:
        return None
    slice_numbers = numbers[37:77]
    unique_numbers = list(set(slice_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]