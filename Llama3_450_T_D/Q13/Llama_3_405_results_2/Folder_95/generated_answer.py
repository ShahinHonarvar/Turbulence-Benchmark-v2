def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    slice_of_numbers = numbers[82:87]
    slice_of_numbers.sort()
    if len(slice_of_numbers) < 2:
        return None
    return slice_of_numbers[-2]