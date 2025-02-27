def find_n_th_smallest_num(numbers):
    slice_of_numbers = numbers[23:66]
    sorted_slice = sorted(slice_of_numbers)
    return sorted_slice[7]