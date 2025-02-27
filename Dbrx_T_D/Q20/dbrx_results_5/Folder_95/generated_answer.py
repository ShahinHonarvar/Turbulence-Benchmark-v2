import heapq

def find_n_th_smallest_num(numbers):
    slice_of_numbers = numbers[44:49]
    return heapq.nsmallest(5, slice_of_numbers)[-1]