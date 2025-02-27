def find_second_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    selected_numbers = numbers[10:101]
    selected_numbers.sort()
    if len(selected_numbers) < 2:
        return None
    return selected_numbers[1]