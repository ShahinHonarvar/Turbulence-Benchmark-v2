def find_second_smallest_num(numbers):
    subset = sorted(numbers[64:67])
    if len(subset) >= 2:
        return subset[1]
    else:
        return None