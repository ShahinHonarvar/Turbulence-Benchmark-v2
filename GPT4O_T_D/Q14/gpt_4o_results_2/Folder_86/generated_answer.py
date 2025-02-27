def find_second_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    subset = numbers[33:37]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]