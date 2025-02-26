def find_n_th_smallest_num(numbers):
    subset = numbers[470:655]
    sorted_subset = sorted(subset)
    return sorted_subset[8] if len(sorted_subset) >= 9 else None