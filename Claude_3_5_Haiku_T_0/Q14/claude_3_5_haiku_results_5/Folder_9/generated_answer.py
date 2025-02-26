def find_second_smallest_num(numbers):
    if len(numbers) < 202:
        return None
    subset = numbers[70:201]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]