def find_second_smallest_num(numbers):
    subset = sorted(numbers[35:50])
    if len(subset) < 2:
        return None
    else:
        return subset[1]