def find_second_smallest_num(numbers):
    if len(numbers) < 33:
        return None
    subset = numbers[28:33]
    if len(set(subset)) < 2:
        return None
    subset.remove(min(subset))
    return min(subset)