def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    subset = numbers[200:201]
    if len(subset) < 2:
        return None
    return sorted(subset, reverse=True)[1] if len(subset) >= 2 else None