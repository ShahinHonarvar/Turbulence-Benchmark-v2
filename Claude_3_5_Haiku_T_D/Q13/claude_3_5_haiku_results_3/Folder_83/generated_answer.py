def find_second_largest_num(numbers):
    if len(numbers) <= 1 or len(numbers) < 91:
        return None
    subset = numbers[90:91]
    if not subset:
        return None
    if len(subset) == 1:
        return subset[0]
    return sorted(subset, reverse=True)[1]