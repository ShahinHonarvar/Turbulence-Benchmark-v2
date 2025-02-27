def find_second_largest_num(numbers):
    try:
        slice_of_numbers = numbers[29:52]
        unique_numbers = set(slice_of_numbers)
        if len(unique_numbers) < 2:
            return None
        else:
            return sorted(unique_numbers)[-2]
    except IndexError:
        return None