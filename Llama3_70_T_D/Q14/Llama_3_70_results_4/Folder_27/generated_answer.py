def find_second_smallest_num(numbers):
    if len(numbers) < 60:
        return None
    return sorted(numbers[25:60])[1] if len(set(numbers[25:60])) > 1 else None