def find_n_th_smallest_num(numbers):
    subset = numbers[11:25]
    sorted_subset = sorted(subset)
    return sorted_subset[9] if len(sorted_subset) >= 10 else None