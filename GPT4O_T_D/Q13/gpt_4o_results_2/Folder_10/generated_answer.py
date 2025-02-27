def find_second_largest_num(numbers):
    if len(numbers) < 60:
        return None
    sublist = numbers[25:60]
    unique_sorted = sorted(set(sublist), reverse=True)
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]