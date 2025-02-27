def find_second_largest_num(numbers):
    if len(numbers) < 687 or not all((isinstance(x, (int, float)) for x in numbers)):
        return None
    sliced_numbers = numbers[686:988]
    unique_numbers = set(sliced_numbers)
    if len(unique_numbers) < 2:
        return None
    return sorted(unique_numbers)[-2]