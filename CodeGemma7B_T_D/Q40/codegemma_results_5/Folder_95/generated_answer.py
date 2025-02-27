def return_n_smallest_chars(distinct_chars):
    sorted_list = sorted(distinct_chars, key=ord)
    return sorted_list[:36]