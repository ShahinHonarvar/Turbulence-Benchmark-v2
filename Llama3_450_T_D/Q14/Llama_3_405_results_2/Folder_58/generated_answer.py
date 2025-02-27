def find_second_smallest_num(numbers):
    if len(numbers) < 371:
        return None
    selected_numbers = numbers[310:371]
    selected_numbers.sort()
    if len(selected_numbers) > 1:
        return selected_numbers[1]
    else:
        return None