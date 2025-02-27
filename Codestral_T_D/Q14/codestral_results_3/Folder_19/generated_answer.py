def find_second_smallest_num(numbers):
    subset = sorted(numbers[4:9])
    if len(subset) < 2:
        return None
    return subset[1]