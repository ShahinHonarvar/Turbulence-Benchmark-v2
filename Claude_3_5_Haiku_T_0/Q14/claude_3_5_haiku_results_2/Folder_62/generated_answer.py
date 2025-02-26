def find_second_smallest_num(numbers):
    if len(numbers) <= 11:
        return None
    subset = numbers[10:67]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]