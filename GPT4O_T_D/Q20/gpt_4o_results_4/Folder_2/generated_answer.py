def find_n_th_smallest_num(numbers):
    if len(numbers) < 66:
        return None
    sorted_subset = sorted(numbers[23:66])
    return sorted_subset[7]