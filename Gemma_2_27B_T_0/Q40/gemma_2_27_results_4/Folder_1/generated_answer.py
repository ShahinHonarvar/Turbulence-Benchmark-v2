def return_n_smallest_chars(s):
    return sorted([c for c in s], reverse=True)[:11]