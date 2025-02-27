def find_second_smallest_num(numbers):
    slice_numbers = numbers[8:10]
    slice_numbers.sort()
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]