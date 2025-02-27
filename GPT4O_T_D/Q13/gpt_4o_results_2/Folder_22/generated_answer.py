def find_second_largest_num(numbers):
    sublist = numbers[40:201]
    if len(sublist) < 2:
        return None
    unique_sorted = sorted(set(sublist), reverse=True)
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]