def find_second_largest_num(numbers):
    if len(numbers) < 55 or 27 > len(numbers):
        return None
    slice_of_numbers = numbers[27:56]
    if len(slice_of_numbers) < 2:
        return None
    slice_of_numbers.sort(reverse=True)
    return slice_of_numbers[1]