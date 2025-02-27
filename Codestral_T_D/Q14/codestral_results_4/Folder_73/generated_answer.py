def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    slice_numbers = numbers[59:98]
    slice_numbers.sort()
    if len(slice_numbers) > 1:
        return slice_numbers[1]
    return None