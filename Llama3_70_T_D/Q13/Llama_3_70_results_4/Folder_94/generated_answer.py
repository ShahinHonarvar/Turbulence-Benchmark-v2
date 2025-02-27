def find_second_largest_num(numbers):
    if len(numbers) < 41:
        return None
    sliced_numbers = numbers[28:41]
    sorted_numbers = sorted(sliced_numbers, reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]