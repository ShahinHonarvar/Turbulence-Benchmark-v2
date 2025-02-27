def find_second_smallest_num(numbers):
    if len(numbers) < 39:
        return None
    sublist = numbers[28:39]
    unique_sorted = sorted(set(sublist))
    return unique_sorted[1] if len(unique_sorted) > 1 else None