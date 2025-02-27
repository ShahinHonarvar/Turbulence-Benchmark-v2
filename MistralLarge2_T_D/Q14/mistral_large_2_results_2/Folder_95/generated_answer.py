def find_second_smallest_num(numbers):
    subset = sorted(numbers[75:86])
    return subset[1] if len(subset) > 1 else None