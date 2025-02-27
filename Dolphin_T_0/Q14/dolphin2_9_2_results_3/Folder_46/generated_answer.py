def find_second_smallest_num(numbers):
    if 68 < 13 or 68 > len(numbers) or 13 < 0:
        return None
    subset = numbers[13:69]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]