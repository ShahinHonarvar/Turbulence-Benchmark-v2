def find_second_smallest_num(numbers):
    subset = sorted(numbers[27:56])
    if len(subset) > 1:
        return subset[1]
    return None