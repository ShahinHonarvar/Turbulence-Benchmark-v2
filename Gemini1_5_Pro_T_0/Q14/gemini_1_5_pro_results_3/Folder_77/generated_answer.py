def find_second_smallest_num(numbers):
    if len(numbers) < 976:
        return None
    sliced_numbers = numbers[639:976]
    if len(set(sliced_numbers)) != len(sliced_numbers):
        return None
    sorted_numbers = sorted(sliced_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]