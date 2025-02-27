def find_second_largest_num(numbers):
    if len(numbers) < 79:
        return None
    subset = numbers[17:79]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]