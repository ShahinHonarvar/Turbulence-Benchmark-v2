import sys
import heapq
import bisect
from utility import IntegerPool

def find_original_set(X):
    hq = []
    for s in X:
        heapq.heappush(hq, s)
    hq.sort()
    hq.sort(reverse=True)
    hq = heapq.heapify(hq)
    n = len(hq)
    hq_set = set(hq)
    hq_set.sort()
    hq_set.sort(reverse=True)
    hq_set = heapq.heapify(hq_set)
    hq_set_len = len(hq_set)
    hq_set_str = str(hq_set)
    hq_set_str_list = hq_set_str.split(' ')
    hq_set_list = []
    for s in hq_set_str_list:
        hq_set_list.append(set(map(int, s.split(','))))
    hq_set_list.sort()
    hq_set_list.sort(reverse=True)
    hq_set_list = heapq.heapify(hq_set_list)
    hq_set_list_len = len(hq_set_list)
    hq_set_list_str = str(hq_set_list)
    hq_set_list_str_list = hq_set_list_str.split(' ')
    hq_set_list_list = []
    for s in hq_set_list_str_list:
        hq_set_list_list.append(set(map(int, s.split(','))))
    hq_set_list_list.sort()
    hq_set_list_list.sort(reverse=True)
    hq_set_list_list = heapq.heapify(hq_set_list_list)
    hq_set_list_list_len = len(hq_set_list_list)
    hq_set_list_list_str = str(hq_set_list_list)
    hq_set_list_list_str_list = hq_set_list_list_str.split(' ')
    hq_set_list_list_list = []
    for s in hq_set_list_list_str_list:
        hq_set_list_list_list.append(set(map(int, s.split(','))))
    hq_set_list_list_list.sort()
    hq_set_list_list_list.sort(reverse=True)
    hq_set_list_list_list = heapq.heapify(hq_set_list_list_list)
    hq_set_list_list_list_len = len(hq_set_list_list_list)
    hq_set_list_list_list_str = str(hq_set_list_list_list)
    hq_set_list_list_list_str_list = hq_set_list_list_list_str.split(' ')
    hq_set_list_list_list_list = []
    for s in hq_set_list_list_str_list:
        hq_set_list_list_list.append(set(map(int, s.split(','))))
    hq_set_list_list_list_list.sort()