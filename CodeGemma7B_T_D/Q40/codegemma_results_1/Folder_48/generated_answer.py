def return_n_smallest_chars(strin):
    return sorted(strin, key=ord)[:12]