def find_second_largest_num(numbers):
    slice_numbers = numbers[33:37]
    if len(slice_numbers) < 2:
        return None
    slice_numbers.sort(reverse=True)
    return slice_numbers[1]