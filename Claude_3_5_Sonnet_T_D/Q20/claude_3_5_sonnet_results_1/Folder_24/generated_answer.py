def find_n_th_smallest_num(numbers):
    subset = numbers[43:81]
    sorted_subset = sorted(subset)
    return sorted_subset[5] if len(sorted_subset) >= 6 else None