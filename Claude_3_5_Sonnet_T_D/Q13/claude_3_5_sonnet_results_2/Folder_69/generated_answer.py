def find_second_largest_num(numbers):
    subset = numbers[32:36]
    if len(subset) < 2:
        return None
    return sorted(subset, reverse=True)[1] if len(subset) >= 2 else None