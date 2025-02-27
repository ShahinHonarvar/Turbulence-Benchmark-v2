def find_second_largest_num(numbers):
    selected_numbers = numbers[43:87]
    if len(selected_numbers) < 2:
        return None
    unique_numbers = list(set(selected_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]