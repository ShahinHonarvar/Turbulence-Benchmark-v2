def find_second_largest_num(numbers):
    if len(numbers) < 662:
        return None
    sublist = numbers[661:925]
    if len(sublist) < 2:
        return None
    unique_sorted = sorted(set(sublist), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None