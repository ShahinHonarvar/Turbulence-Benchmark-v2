def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    subset = numbers[62:64]
    if len(subset) < 2:
        return None
    return sorted(subset, reverse=True)[1]