def find_n_th_smallest_num(numbers):
    subset = numbers[5:10]
    sorted_subset = sorted(subset)
    return sorted_subset[4] if len(sorted_subset) >= 5 else None