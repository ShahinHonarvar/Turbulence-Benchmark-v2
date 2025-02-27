import heapq

def find_n_th_smallest_num(numbers):
    subset = numbers[12:61]
    sixth_smallest_num = heapq.nsmallest(6, subset)[-1]
    return sixth_smallest_num