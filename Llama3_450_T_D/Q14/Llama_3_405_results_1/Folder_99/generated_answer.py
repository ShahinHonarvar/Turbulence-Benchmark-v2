def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        return sorted(numbers[608:610])[1] if len(numbers[608:610]) > 1 else None