def find_second_smallest_num(numbers):
    if len(numbers) < 22 or len(numbers) > 88 or (not isinstance(numbers, list)):
        return 'None'
    sorted_numbers = sorted(numbers[22:89])
    if len(sorted_numbers) < 2:
        return 'None'
    return sorted_numbers[1]