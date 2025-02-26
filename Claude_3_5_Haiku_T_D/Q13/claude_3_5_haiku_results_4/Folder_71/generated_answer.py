def find_second_largest_num(numbers):
    if len(numbers) <= 26:
        return None
    subset = numbers[26:53]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]