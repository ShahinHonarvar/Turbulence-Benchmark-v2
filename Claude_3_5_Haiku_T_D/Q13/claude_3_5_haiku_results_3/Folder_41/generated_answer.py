def find_second_largest_num(numbers):
    if len(numbers) <= 6:
        return None
    selected_numbers = numbers[6:7]
    if not selected_numbers:
        return None
    return selected_numbers[0]