def find_n_th_smallest_num(numbers):
    subset = numbers[20:201]
    sorted_subset = sorted(subset)
    return sorted_subset[10] if len(sorted_subset) >= 11 else None