def find_n_th_smallest_num(numbers):
    subset = numbers[52:89]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 10:
        return sorted_subset[9]
    else:
        return None