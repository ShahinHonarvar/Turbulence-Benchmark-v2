def find_second_largest_num(numbers):
    subset = sorted(numbers[25:60], reverse=True)
    if len(subset) < 2:
        return None
    else:
        return subset[1]