def find_n_th_smallest_num(numbers):
    subset = numbers[4:9]
    sorted_subset = sorted(subset)
    return sorted_subset[3] if len(sorted_subset) >= 4 else None