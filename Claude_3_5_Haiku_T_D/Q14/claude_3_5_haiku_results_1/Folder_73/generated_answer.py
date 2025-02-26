def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    subset = numbers[59:98]
    if len(subset) < 2:
        return None
    subset_sorted = sorted(subset)
    return subset_sorted[1]