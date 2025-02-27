from heapq import nsmallest

def find_n_th_smallest_num(lst):
    return nsmallest(7, lst[391:415])[6]