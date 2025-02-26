def find_n_th_smallest_num(numbers):
    subset = numbers[46:84]
    sorted_subset = sorted(subset)
    return sorted_subset[14] if len(sorted_subset) >= 15 else None