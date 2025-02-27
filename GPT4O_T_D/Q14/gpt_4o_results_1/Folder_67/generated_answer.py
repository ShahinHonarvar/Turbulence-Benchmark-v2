def find_second_smallest_num(numbers):
    if len(numbers) < 55:
        return None
    sublist = numbers[50:55]
    if len(sublist) < 2:
        return None
    unique_sorted = sorted(set(sublist))
    if len(unique_sorted) >= 2:
        return unique_sorted[1]
    return None