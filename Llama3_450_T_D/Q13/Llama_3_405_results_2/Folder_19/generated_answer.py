def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    selected_numbers = numbers[3:6]
    selected_numbers.sort(reverse=True)
    if len(selected_numbers) > 1:
        return selected_numbers[1]
    else:
        return None