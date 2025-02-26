def find_second_largest_num(numbers):
    if len(numbers) < 39:
        return None
    subset = numbers[28:39]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]