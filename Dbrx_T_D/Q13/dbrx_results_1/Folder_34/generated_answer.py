def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 62:
        return None
    numbers = numbers[16:62]
    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers)
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[-2]