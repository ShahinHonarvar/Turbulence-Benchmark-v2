def find_second_smallest_num(numbers):
    if 88 < len(numbers) < 75:
        return None
    else:
        return sorted(numbers[75:89])[1] if len(numbers[75:89]) > 1 else None