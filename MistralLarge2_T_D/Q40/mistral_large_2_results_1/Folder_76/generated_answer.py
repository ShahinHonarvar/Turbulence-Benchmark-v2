def return_n_smallest_chars(s):
    return sorted(s, key=ord)[:3][::-1]