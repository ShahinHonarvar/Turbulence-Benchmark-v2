def find_second_smallest_num(numbers):
    subset = sorted(numbers[20:201])
    return subset[1] if len(subset) > 1 else None