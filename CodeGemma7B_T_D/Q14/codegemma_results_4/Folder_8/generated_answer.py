def find_second_smallest_num(numbers):
    if len(numbers) <= 66:
        return None
    sorted_numbers = sorted(numbers[56:67])
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None