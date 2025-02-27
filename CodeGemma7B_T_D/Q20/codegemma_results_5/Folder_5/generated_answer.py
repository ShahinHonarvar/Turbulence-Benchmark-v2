def find_n_th_smallest_num(a):
    a.sort(key=int)
    return a[4]