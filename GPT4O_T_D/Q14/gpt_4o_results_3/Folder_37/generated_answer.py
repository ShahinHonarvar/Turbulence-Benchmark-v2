def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    window = numbers[5:8]
    if len(window) < 2:
        return None
    unique_sorted = sorted(set(window))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]