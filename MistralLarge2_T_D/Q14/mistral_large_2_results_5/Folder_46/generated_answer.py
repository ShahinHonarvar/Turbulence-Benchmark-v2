def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    subset = numbers[13:69]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]