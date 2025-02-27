def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 750 < 246:
        return None
    return sorted(numbers[246:751])[1] if len(numbers[246:751]) > 1 else None