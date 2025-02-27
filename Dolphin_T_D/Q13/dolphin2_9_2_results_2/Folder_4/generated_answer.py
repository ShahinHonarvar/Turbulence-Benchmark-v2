def find_second_largest_num(numbers):
    if 12 <= 92 < len(numbers):
        subset = sorted(numbers[12:93], reverse=True)
        if len(subset) > 1:
            return subset[1]
    return None