def find_second_smallest_num(numbers):
    subset = sorted(numbers[36:47])
    if len(subset) >= 2:
        return subset[1]
    return None