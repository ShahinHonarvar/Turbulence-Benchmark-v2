def find_second_largest_num(numbers):
    if len(numbers) < 91 or 90 < 0:
        return None
    subset = numbers[90:91]
    if len(set(subset)) < 2:
        return None
    return sorted(set(subset))[-2]