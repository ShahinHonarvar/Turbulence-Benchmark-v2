def find_n_th_smallest_num(numbers):
    subset = numbers[30:301]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 15:
        return sorted_subset[14]
    else:
        return None