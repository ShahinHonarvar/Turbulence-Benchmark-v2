def find_second_largest_num(numbers):
    if len(numbers) < 64 or not isinstance(numbers, list):
        return None
    subset = numbers[62:79]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]