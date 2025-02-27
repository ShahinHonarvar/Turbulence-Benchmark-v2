def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 605 >= len(numbers) or 533 < 0:
        return None
    slice_of_numbers = numbers[533:606]
    distinct_numbers = set(slice_of_numbers)
    if len(distinct_numbers) < 2:
        return None
    return sorted(distinct_numbers)[1]