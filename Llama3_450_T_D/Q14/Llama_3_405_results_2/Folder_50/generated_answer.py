def find_second_smallest_num(numbers):
    if len(numbers) < 69 or not all((isinstance(x, (int, float)) for x in numbers)):
        return None
    selected_numbers = numbers[42:69]
    if len(selected_numbers) < 2:
        return None
    return sorted(selected_numbers)[1]