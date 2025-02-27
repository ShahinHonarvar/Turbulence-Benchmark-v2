def find_second_smallest_num(numbers):
    if len(numbers) < 33:
        return None
    subset = sorted(numbers[28:33])
    return subset[1] if len(subset) > 1 else None