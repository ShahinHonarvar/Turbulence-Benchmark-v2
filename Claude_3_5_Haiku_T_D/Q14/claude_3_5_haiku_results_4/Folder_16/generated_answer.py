def find_second_smallest_num(numbers):
    if len(numbers) < 78:
        return None
    subset = numbers[66:78]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]