def find_second_largest_num(numbers):
    if len(numbers) < 91:
        return None
    subset = numbers[90:91]
    subset = list(set(subset))
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]