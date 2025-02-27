def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    sublist = numbers[10:11]
    if len(sublist) < 2:
        return None
    unique_sorted = sorted(set(sublist))
    return unique_sorted[1] if len(unique_sorted) >= 2 else None