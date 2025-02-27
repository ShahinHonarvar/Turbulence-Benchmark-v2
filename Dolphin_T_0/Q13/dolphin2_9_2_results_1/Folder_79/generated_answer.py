def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        slice_of_numbers = numbers[4:5]
        if len(slice_of_numbers) != 1:
            return None
        else:
            sorted_slice = sorted(slice_of_numbers, reverse=True)
            return sorted_slice[1]