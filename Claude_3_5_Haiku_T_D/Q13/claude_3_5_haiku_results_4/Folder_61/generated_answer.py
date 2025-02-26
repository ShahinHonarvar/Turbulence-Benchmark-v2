def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 8:
        return None
    sublist = numbers[0:8]
    unique_sorted = sorted(set(sublist), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None