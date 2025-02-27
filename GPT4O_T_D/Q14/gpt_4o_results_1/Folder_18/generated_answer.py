def find_second_smallest_num(numbers):
    selected_numbers = numbers[30:49]
    if len(selected_numbers) < 2:
        return None
    unique_numbers = sorted(set(selected_numbers))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]