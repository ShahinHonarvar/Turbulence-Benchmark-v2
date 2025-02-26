def find_n_th_smallest_num(numbers):
    sorted_subset = sorted(numbers[16:74])
    return sorted_subset[14] if len(sorted_subset) >= 15 else None