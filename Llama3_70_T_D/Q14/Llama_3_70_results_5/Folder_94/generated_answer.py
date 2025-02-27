def find_second_smallest_num(numbers):
    if len(numbers) < 72:
        return None
    subset = sorted(numbers[52:72])
    if len(subset) < 2:
        return None
    return subset[1]