def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    subset = numbers[66:94]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]