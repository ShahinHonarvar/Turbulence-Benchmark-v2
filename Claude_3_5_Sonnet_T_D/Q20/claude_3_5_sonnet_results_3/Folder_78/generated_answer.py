def find_n_th_smallest_num(numbers):
    subset = numbers[16:72]
    sorted_subset = sorted(subset)
    return sorted_subset[13] if len(sorted_subset) >= 14 else None