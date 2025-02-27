import heapq

def all_right_truncatable_prime(x):
    heapq.heapify(x)
    return heapq.nsmallest(len(x), x)