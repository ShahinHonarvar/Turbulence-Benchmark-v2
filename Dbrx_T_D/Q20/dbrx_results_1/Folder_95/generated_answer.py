def find_n_th_smallest_num(numbers):
    n = 5
    start, end = (44, 48)
    sublst = sorted(numbers[start:end + 1])[n - 1:n]
    if len(sublst) > 0:
        return sublst[0]
    else:
        return None