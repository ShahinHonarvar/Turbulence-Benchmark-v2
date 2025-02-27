def find_n_th_smallest_num(numbers):
    n = 14
    start = 24
    end = 37
    return sorted(numbers[start:end + 1])[n - 1]