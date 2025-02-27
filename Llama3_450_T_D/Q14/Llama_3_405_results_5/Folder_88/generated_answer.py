def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    selected_numbers = numbers[6:9]
    selected_numbers.sort()
    if len(selected_numbers) < 2:
        return None
    return selected_numbers[1]