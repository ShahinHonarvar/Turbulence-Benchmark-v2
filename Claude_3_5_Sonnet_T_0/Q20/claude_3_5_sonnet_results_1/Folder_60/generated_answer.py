def find_n_th_smallest_num(numbers):
    subset = numbers[16:74]
    sorted_subset = sorted(subset)
    return sorted_subset[14] if len(sorted_subset) >= 15 else None