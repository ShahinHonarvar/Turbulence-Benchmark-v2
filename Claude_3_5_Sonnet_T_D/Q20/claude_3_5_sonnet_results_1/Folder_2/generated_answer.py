def find_n_th_smallest_num(numbers):
    subset = numbers[23:66]
    sorted_subset = sorted(subset)
    return sorted_subset[7] if len(sorted_subset) >= 8 else None