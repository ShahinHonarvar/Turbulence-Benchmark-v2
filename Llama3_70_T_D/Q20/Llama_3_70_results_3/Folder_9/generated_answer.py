def find_n_th_smallest_num(numbers):
    n = 10
    return sorted(numbers[9:101])[n - 1]