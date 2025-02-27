def find_second_smallest_num(numbers):
    if len(numbers) < 23:
        return None
    sorted_numbers = sorted(list(set(numbers[23:])) + [numbers[23]])
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]