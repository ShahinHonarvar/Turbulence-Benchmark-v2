def find_second_smallest_num(numbers):
    if len(numbers) < 609:
        return None
    return sorted(numbers[608:610])[1] if len(set(numbers[608:610])) > 1 else None