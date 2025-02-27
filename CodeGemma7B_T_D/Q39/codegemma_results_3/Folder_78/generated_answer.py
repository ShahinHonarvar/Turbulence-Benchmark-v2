from heapq import nlargest

def return_n_greatest_chars(str_of_distinct_chars):
    return nlargest(43, str_of_distinct_chars, key=ord)