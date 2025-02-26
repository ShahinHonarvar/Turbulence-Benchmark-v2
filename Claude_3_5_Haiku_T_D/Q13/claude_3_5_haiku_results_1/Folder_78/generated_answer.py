def find_second_largest_num(numbers):
    if len(numbers) <= 43:
        return None
    subset = numbers[43:52]
    if len(subset) == 0:
        return None
    subset.sort(reverse=True)
    return subset[1] if len(subset) > 1 else None