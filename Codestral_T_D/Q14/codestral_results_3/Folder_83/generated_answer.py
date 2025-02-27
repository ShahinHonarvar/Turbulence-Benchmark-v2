def find_second_smallest_num(numbers):
    subset = sorted(numbers[90:201])
    if len(subset) < 2:
        return None
    else:
        return subset[1]