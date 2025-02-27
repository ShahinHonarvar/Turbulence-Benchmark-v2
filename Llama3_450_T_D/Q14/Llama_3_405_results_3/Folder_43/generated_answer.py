def find_second_smallest_num(numbers):
    if len(numbers) < 96:
        return None
    slice_of_numbers = numbers[74:96]
    if len(slice_of_numbers) < 2:
        return None
    slice_of_numbers.sort()
    return slice_of_numbers[1]