def find_n_th_smallest_num(lst):
    filtered = [i for i in lst[20:201]]
    return sorted(filtered)[10]