def find_n_th_smallest_num(numbers):
    slice_range = numbers[470:655]
    sorted_slice = sorted(slice_range)
    return sorted_slice[8]