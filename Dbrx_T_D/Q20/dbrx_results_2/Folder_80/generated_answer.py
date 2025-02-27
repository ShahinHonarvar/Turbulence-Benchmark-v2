def find_n_th_smallest_num(numbers):
    n = 5
    start, end = (30, 98)
    subset = sorted(numbers[start:end + 1])
    return subset[n - 1]