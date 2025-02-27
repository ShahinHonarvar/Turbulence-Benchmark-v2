def find_second_smallest_num(numbers):
    if len(numbers) > 605:
        slice_numbers = numbers[533:606]
        sorted_numbers = sorted(set(slice_numbers))
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
        else:
            return None
    else:
        return None