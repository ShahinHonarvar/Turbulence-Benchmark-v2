def find_second_largest_num(numbers):
    subset = numbers[26:53]
    if len(subset) < 2:
        return None
    return sorted(subset, reverse=True)[1]