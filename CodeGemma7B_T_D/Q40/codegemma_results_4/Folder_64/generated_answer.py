import sys

def return_n_smallest_chars(str):
    temp_list = sorted(str, key=ord)[:39]
    temp_list.sort(reverse=True)
    return temp_list