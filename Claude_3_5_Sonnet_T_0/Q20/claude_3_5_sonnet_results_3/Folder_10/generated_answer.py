def find_n_th_smallest_num(numbers):
    subset = numbers[56:97]
    sorted_subset = sorted(subset)
    return sorted_subset[17] if len(sorted_subset) >= 18 else None