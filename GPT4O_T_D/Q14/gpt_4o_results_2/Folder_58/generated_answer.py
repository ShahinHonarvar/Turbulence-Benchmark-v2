def find_second_smallest_num(numbers):
    sublist = numbers[310:371]
    if len(sublist) < 2:
        return None
    unique_sorted = sorted(set(sublist))
    return unique_sorted[1] if len(unique_sorted) > 1 else None