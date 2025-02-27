def find_second_smallest_num(numbers):
    slice_of_numbers = numbers[28:39]
    if len(slice_of_numbers) < 2:
        return None
    else:
        slice_of_numbers.sort()
        return slice_of_numbers[1]