def find_n_th_smallest_num(numbers):
    subset = numbers[21:70]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 10:
        return sorted_subset[9]
    else:
        return None