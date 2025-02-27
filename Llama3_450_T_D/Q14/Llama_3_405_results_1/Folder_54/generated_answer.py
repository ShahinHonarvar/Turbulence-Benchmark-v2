def find_second_smallest_num(numbers):
    if len(numbers) < 87 or not all((isinstance(x, (int, float)) for x in numbers)):
        return None
    selected_numbers = numbers[68:87]
    sorted_numbers = sorted(set(selected_numbers))
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]