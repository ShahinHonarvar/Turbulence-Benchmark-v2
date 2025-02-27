def return_n_smallest_chars(S):
    return sorted(S, key=lambda x: ord(x))[:43]