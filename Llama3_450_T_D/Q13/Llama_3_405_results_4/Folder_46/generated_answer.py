def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    selected_numbers = numbers[30:88]
    if len(selected_numbers) < 2:
        return None
    return sorted(selected_numbers)[-2]