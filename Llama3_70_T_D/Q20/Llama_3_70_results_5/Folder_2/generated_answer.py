def find_n_th_smallest_num(numbers):
    target_slice = numbers[23:66]
    target_slice.sort()
    return target_slice[7]