def find_second_largest_num(numbers):
    if len(numbers) < 65 or 14 >= len(numbers):
        return None
    sliced_numbers = numbers[14:65]
    if len(set(sliced_numbers)) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[-2]