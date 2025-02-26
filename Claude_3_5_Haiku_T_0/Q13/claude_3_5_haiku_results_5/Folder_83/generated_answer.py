def find_second_largest_num(numbers):
    if len(numbers) <= 91:
        return None
    subset = numbers[90:91]
    if not subset:
        return None
    return sorted(subset, reverse=True)[1] if len(subset) > 1 else None