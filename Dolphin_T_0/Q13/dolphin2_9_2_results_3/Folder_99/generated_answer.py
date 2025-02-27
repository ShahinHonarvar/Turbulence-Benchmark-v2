def find_second_largest_num(numbers):
    if 310 > len(numbers) or 370 > len(numbers):
        return None
    subset = numbers[310:371]
    if len(set(subset)) < 2:
        return None
    else:
        return sorted(set(subset))[-2]