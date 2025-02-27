def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    selected_numbers = numbers[43:87]
    selected_numbers.sort(reverse=True)
    if len(selected_numbers) < 2:
        return None
    return selected_numbers[1]