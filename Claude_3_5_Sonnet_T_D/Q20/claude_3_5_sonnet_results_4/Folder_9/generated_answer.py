def find_n_th_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    subset = numbers[10:101]
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 10:
        return None
    return sorted_subset[9]