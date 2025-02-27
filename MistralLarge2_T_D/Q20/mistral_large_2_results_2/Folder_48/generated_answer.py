def find_n_th_smallest_num(numbers):
    subset = numbers[127:849]
    subset.sort()
    return subset[9]