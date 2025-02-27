def find_second_largest_num(numbers):
    if len(numbers) < 89 or 22 > len(numbers):
        return None
    slice_of_numbers = numbers[22:89]
    slice_of_numbers.sort(reverse=True)
    if len(slice_of_numbers) < 2:
        return None
    return slice_of_numbers[1]