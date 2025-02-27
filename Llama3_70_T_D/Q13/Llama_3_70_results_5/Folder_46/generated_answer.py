def find_second_largest_num(numbers):
    slice_numbers = numbers[30:88]
    if len(slice_numbers) < 2:
        return None
    else:
        slice_numbers.sort(reverse=True)
        return slice_numbers[1]