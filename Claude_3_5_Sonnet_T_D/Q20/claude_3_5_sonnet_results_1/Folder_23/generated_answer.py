def find_n_th_smallest_num(numbers):
    subset = numbers[14:97]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 13:
        return sorted_subset[12]
    else:
        return None