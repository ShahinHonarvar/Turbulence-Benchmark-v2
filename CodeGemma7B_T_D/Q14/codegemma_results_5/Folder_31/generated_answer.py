from heapq import nsmallest

def find_second_smallest_num(lst):
    sorted_lst = sorted(lst[29:94])
    if len(sorted_lst) < 2:
        return None
    else:
        return sorted_lst[1]