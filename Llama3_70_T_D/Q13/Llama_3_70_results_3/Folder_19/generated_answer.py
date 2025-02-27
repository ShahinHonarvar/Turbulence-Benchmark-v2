def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    return sorted(numbers[3:6])[-2] if len(set(numbers[3:6])) > 1 else None