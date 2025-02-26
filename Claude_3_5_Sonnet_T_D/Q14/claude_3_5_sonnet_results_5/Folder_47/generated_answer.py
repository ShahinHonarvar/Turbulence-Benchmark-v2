def find_second_smallest_num(numbers):
    subset = numbers[22:64]
    if len(subset) < 2:
        return None
    return sorted(set(subset))[1] if len(set(subset)) > 1 else None