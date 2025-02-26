def find_n_th_smallest_num(numbers):
    slice = numbers[23:46]
    sorted_slice = sorted(slice)
    return sorted_slice[6] if len(sorted_slice) >= 7 else None