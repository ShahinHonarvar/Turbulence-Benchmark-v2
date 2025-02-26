def find_n_th_smallest_num(numbers):
    subset = numbers[85:100]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 7:
        return sorted_subset[6]
    else:
        return None