def find_n_th_smallest_num(lst):
    return sorted(lst[61:88], key=lambda x: abs(x))[6]