def find_second_largest_num(numbers):
    slice_of_numbers = numbers[29:52]
    if len(slice_of_numbers) < 2:
        return None
    slice_of_numbers.sort(reverse=True)
    return slice_of_numbers[1]