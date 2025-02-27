def find_second_smallest_num(numbers):
    if len(numbers) <= 63:
        return None
    else:
        slice_numbers = sorted(numbers[22:64])
        if len(slice_numbers) < 2:
            return None
        else:
            return slice_numbers[1]