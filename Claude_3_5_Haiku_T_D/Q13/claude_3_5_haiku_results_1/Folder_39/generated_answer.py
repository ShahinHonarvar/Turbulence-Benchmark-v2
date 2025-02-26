def find_second_largest_num(numbers):
    if len(numbers) <= 20:
        return None
    sublist = numbers[20:31]
    unique_sorted = sorted(set(sublist), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None