def find_n_th_smallest_num(numbers):
    subset = numbers[213:323]
    sorted_subset = sorted(subset)
    return sorted_subset[7] if len(sorted_subset) >= 8 else None