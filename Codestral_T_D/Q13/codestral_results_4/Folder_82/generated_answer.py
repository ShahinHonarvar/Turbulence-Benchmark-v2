def find_second_largest_num(numbers):
    subset = sorted(numbers[20:201], reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]