def find_n_th_smallest_num(numbers):
    subset = numbers[19:191]
    sorted_subset = sorted(subset)
    return sorted_subset[18]