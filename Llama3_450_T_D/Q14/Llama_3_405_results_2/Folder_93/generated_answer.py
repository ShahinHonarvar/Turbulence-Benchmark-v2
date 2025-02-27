def find_second_smallest_num(numbers):
    if len(numbers) < 89:
        return None
    selected_numbers = numbers[75:89]
    selected_numbers.sort()
    if len(selected_numbers) < 2:
        return None
    return selected_numbers[1]