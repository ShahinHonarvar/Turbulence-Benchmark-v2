def find_n_th_smallest_num(numbers):
    n = 4
    start, end = (59, 74)
    sub_numbers = sorted(numbers[start:end + 1])
    return sub_numbers[n - 1]