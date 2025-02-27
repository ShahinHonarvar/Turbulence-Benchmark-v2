def return_n_smallest_chars(str_distinct):
    return sorted(str_distinct, key=ord)[:43]