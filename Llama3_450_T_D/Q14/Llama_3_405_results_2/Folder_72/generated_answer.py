def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    selected_numbers = numbers[82:87]
    sorted_numbers = sorted(selected_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]