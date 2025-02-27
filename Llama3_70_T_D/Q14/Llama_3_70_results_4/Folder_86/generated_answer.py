def find_second_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    subset = numbers[33:37]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]