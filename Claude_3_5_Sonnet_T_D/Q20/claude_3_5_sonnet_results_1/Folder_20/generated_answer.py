def find_n_th_smallest_num(numbers):
    subset = numbers[25:65]
    sorted_subset = sorted(subset)
    return sorted_subset[11] if len(sorted_subset) >= 12 else None