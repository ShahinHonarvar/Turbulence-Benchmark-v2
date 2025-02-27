def find_second_largest_num(numbers):
    if len(numbers) < 69:
        return None
    sublist = numbers[13:69]
    if len(sublist) < 2:
        return None
    unique_sorted = sorted(set(sublist), reverse=True)
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]