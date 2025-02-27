def find_second_largest_num(numbers):
    slice_of_numbers = numbers[5:8]
    if len(slice_of_numbers) < 2:
        return None
    else:
        slice_of_numbers.remove(max(slice_of_numbers))
        return max(slice_of_numbers)