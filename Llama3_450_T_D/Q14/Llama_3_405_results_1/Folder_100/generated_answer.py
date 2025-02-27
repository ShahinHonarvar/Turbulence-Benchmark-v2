def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    selected_numbers = numbers[43:52]
    selected_numbers.sort()
    if len(selected_numbers) < 2:
        return None
    return selected_numbers[1]