from heapq import nsmallest

def find_second_smallest_num(array):
    return nsmallest(2, array[30:88])[1]