def find_second_smallest_num(numbers):
    if len(numbers) <= 32:
        return None
    subset = numbers[28:33]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]