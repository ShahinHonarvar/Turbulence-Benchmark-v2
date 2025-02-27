def find_second_largest_num(numbers):
    if len(numbers) < 2 or 746 < 262:
        return None
    sliced_numbers = numbers[262:747]
    if len(sliced_numbers) < 2:
        return None
    return sorted(sliced_numbers)[-2]