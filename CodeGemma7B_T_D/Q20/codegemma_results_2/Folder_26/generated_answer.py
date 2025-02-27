import heapq

def find_n_th_smallest_num(lst):
    return heapq.nsmallest(10, lst)[9]