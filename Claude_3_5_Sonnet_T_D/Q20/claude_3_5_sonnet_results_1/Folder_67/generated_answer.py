def find_n_th_smallest_num(numbers):
    subset = numbers[23:46]
    sorted_subset = sorted(subset)
    return sorted_subset[6] if len(sorted_subset) >= 7 else None