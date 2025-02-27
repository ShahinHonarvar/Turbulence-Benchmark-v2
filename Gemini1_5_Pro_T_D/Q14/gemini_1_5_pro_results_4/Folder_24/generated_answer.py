def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    return sorted(numbers[23:24])[1] if len(numbers[23:24]) > 1 else None