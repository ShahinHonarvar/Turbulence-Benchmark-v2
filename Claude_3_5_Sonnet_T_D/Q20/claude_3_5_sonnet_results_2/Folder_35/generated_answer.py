def find_n_th_smallest_num(numbers):
    sorted_slice = sorted(numbers[12:61])
    return sorted_slice[5] if len(sorted_slice) >= 6 else None