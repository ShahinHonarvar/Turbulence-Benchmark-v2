def find_second_largest_num(numbers):
    if len(numbers) < 101:
        return None
    subset = sorted(numbers[10:101], reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]