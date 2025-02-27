def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 52:
        return None
    slice_numbers = sorted(numbers[14:52])
    if slice_numbers[0] == slice_numbers[-1]:
        return None
    return slice_numbers[-2]