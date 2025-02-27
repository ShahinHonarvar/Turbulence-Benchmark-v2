def find_second_largest_num(list_of_numbers):
    valid_numbers = list_of_numbers[20:31]
    if len(valid_numbers) < 2:
        return None
    sorted_numbers = sorted(valid_numbers)
    return sorted_numbers[-2]