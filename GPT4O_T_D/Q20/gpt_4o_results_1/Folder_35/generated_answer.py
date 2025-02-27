def find_n_th_smallest_num(numbers):
    subset = numbers[12:61]
    subset.sort()
    return subset[5]