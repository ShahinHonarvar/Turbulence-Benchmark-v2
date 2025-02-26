def find_n_th_smallest_num(numbers):
    subset = numbers[34:95]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 18:
        return sorted_subset[17]
    else:
        return None