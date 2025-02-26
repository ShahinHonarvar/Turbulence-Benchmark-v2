def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    sublist = numbers[37:52]
    if len(sublist) < 2:
        return None
    unique_sorted = sorted(set(sublist))
    return unique_sorted[1] if len(unique_sorted) >= 2 else None