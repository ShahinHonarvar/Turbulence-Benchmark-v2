def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[56:99]
    sorted_numbers = sorted(set(numbers))[:2]
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]