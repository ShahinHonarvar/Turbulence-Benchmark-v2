def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    slice_numbers = numbers[68:87]
    slice_numbers.sort(reverse=True)
    if len(slice_numbers) < 2:
        return None
    return slice_numbers[1]