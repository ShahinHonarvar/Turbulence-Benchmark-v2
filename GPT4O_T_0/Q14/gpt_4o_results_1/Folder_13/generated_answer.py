def find_second_smallest_num(numbers):
    if len(numbers) < 33:
        return None
    sublist = numbers[28:33]
    if len(sublist) < 2:
        return None
    unique_sorted = sorted(set(sublist))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]