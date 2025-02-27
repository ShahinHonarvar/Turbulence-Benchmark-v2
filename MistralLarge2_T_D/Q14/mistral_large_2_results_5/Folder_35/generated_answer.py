def find_second_smallest_num(numbers):
    subset = sorted(numbers[15:40])
    if len(subset) < 2:
        return None
    return subset[1]