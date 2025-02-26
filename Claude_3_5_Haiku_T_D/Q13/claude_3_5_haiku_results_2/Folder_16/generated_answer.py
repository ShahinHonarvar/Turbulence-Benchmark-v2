def find_second_largest_num(numbers):
    if len(numbers) < 37:
        return None
    selected_numbers = numbers[33:37]
    if len(selected_numbers) < 2:
        return None
    sorted_numbers = sorted(selected_numbers, reverse=True)
    return sorted_numbers[1]