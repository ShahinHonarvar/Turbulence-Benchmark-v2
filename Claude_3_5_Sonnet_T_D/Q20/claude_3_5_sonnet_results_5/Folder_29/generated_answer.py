def find_n_th_smallest_num(numbers):
    subset = numbers[20:63]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 12:
        return sorted_subset[11]
    else:
        return None