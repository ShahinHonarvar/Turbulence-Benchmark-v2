def find_n_th_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    sorted_subset = sorted(numbers[10:101])
    return sorted_subset[9]