def find_second_smallest_num(numbers):
    if 88 < 22 or 88 >= len(numbers) or 22 < 0:
        return None
    subset = numbers[22:89]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]