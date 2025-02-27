def find_n_th_smallest_num(numbers):
    subset = numbers[26:91]
    subset.sort()
    return subset[3]