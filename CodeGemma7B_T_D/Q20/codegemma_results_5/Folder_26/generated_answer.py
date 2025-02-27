from heapq import nsmallest

def find_n_th_smallest_num(lst):
    return nsmallest(10, lst)[9]