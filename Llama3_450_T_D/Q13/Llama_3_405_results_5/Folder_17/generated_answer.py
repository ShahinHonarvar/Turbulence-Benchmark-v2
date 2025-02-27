def find_second_largest_num(numbers):
    slice_of_numbers = numbers[62:79]
    if len(slice_of_numbers) < 2:
        return None
    else:
        unique_slice_of_numbers = set(slice_of_numbers)
        if len(unique_slice_of_numbers) < 2:
            return None
        else:
            return sorted(unique_slice_of_numbers)[-2]