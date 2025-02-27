def find_second_smallest_num(numbers):
    selected_numbers = numbers[55:99]
    if len(selected_numbers) < 2:
        return None
    return sorted(selected_numbers)[1]