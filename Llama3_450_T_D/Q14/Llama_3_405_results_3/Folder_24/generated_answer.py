def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 23 >= len(numbers):
        return None
    else:
        slice_of_numbers = numbers[23:24]
        slice_of_numbers.sort()
        if len(slice_of_numbers) < 2:
            return None
        else:
            return slice_of_numbers[1]