def find_second_smallest_num(numbers):
    if len(numbers) < 94:
        return None
    else:
        slice_of_numbers = numbers[29:94]
        if len(set(slice_of_numbers)) < 2:
            return None
        else:
            return sorted(set(slice_of_numbers))[1]