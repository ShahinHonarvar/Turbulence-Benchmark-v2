def find_second_smallest_num(numbers):
    selected_numbers = sorted(numbers[56:83])
    if len(selected_numbers) < 2:
        return None
    return selected_numbers[1]