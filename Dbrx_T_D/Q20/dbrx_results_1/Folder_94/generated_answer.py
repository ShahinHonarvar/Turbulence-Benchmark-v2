def find_n_th_smallest_num(numbers):
    n = 6
    slice_indices = slice(57, 71)
    target_numbers = sorted(numbers[slice_indices])[n - 1]
    return target_numbers