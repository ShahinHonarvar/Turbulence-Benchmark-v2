def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    subset = numbers[59:98]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]