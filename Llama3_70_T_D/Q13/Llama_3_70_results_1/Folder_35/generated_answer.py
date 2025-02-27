def find_second_largest_num(numbers):
    if len(numbers) < 49:
        return None
    slice_numbers = numbers[30:49]
    if len(set(slice_numbers)) < 2:
        return None
    slice_numbers = list(set(slice_numbers))
    slice_numbers.sort()
    return slice_numbers[-2]