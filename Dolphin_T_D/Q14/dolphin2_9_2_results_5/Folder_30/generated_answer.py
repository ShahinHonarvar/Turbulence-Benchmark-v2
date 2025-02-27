def find_second_smallest_num(numbers):
    if 52 < len(numbers) < 26:
        return None
    subset = numbers[26:53]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]