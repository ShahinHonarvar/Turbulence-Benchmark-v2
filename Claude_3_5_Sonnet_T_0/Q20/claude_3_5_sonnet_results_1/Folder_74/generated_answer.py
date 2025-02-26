def find_n_th_smallest_num(numbers):
    subset = numbers[12:91]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 17:
        return sorted_subset[16]
    else:
        return None