def return_n_smallest_chars(s):
    return sorted([c for c in s][:7], reverse=True)