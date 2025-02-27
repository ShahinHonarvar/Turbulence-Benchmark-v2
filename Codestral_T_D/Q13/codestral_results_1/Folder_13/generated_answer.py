def find_second_largest_num(numbers):
    subset = sorted(numbers[25:88], reverse=True)
    if len(subset) >= 2:
        return subset[1]
    else:
        return None