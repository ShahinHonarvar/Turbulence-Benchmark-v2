def find_second_smallest_num(numbers):
    if len(numbers) <= 92:
        return None
    subset = numbers[19:93]
    subset = list(set(subset))
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]