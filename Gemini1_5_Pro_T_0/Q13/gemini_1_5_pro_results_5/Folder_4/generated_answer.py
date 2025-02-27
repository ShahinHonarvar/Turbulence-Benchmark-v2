def find_second_largest_num(numbers):
    if len(numbers) < 92:
        return None
    sliced_numbers = numbers[12:93]
    if len(set(sliced_numbers)) != len(sliced_numbers):
        return None
    if len(sliced_numbers) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[-2]