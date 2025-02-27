def return_n_smallest_chars(s):
    return sorted([i for i in s], reverse=True)[:6]