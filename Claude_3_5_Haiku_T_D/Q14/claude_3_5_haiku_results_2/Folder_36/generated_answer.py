def find_second_smallest_num(numbers):
    if len(numbers) < 558:
        return None
    subset = numbers[209:557]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]