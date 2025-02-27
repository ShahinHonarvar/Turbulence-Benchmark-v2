def find_second_largest_num(numbers):
    slice_of_numbers = numbers[25:88]
    if len(slice_of_numbers) < 2:
        return None
    else:
        slice_of_numbers.sort(reverse=True)
        return slice_of_numbers[1]