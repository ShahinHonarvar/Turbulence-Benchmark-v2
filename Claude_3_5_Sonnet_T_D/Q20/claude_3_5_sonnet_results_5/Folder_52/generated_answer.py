def find_n_th_smallest_num(numbers):
    subset = numbers[40:76]
    sorted_subset = sorted(subset)
    return sorted_subset[18] if len(sorted_subset) >= 19 else None