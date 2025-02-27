def find_second_smallest_num(numbers):
    if len(numbers) <= 40:
        return None
    subset = numbers[28:41]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]