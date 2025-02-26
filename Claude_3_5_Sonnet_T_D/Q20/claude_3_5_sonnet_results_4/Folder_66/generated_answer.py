def find_n_th_smallest_num(numbers):
    subset = numbers[11:44]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 16:
        return sorted_subset[15]
    else:
        return None