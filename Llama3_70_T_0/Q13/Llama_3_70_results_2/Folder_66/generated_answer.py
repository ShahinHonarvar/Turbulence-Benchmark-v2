def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    slice_numbers = numbers[50:55]
    slice_numbers.sort(reverse=True)
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]