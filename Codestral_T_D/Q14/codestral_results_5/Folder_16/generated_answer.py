def find_second_smallest_num(numbers):
    selected_numbers = numbers[66:78]
    selected_numbers.sort()
    if len(selected_numbers) >= 2:
        return selected_numbers[1]
    else:
        return None