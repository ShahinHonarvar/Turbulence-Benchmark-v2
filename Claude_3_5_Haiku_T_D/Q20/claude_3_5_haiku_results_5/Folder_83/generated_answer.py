def find_n_th_smallest_num(numbers):
    subset = numbers[30:301]
    sorted_subset = sorted(subset)
    return sorted_subset[14]