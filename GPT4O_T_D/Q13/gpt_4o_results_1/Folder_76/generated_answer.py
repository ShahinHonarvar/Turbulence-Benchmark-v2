def find_second_largest_num(numbers):
    sublist = numbers[686:988]
    unique_sorted = sorted(set(sublist), reverse=True)
    if len(unique_sorted) >= 2:
        return unique_sorted[1]
    return None