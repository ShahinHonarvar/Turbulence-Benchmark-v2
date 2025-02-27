def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    selected_numbers = numbers[43:87]
    if len(selected_numbers) < 2:
        return None
    sorted_numbers = sorted(selected_numbers)
    return sorted_numbers[-2]