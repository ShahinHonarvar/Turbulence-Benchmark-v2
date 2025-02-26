def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    subset = numbers[608:610]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]