def find_second_smallest_num(numbers):
    subset = sorted(numbers[21:98])
    if len(subset) < 2:
        return None
    return subset[1]