def find_n_th_smallest_num(num):
    num.sort()
    small = num[58:75]
    return sorted(small)[3]