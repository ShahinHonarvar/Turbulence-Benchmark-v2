def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    subset = numbers[4:5]
    if len(subset) < 2:
        return None
    return sorted(subset)[1] if len(subset) > 1 else None