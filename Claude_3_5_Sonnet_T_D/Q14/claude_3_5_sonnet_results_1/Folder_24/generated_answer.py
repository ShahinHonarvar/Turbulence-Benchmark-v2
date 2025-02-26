def find_second_smallest_num(numbers):
    if len(numbers) <= 23 or len(numbers[23:24]) < 2:
        return None
    return sorted(numbers[23:24])[1] if len(numbers[23:24]) >= 2 else None