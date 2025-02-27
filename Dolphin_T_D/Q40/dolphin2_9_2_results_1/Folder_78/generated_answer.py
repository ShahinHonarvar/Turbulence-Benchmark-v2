def return_n_smallest_chars(s):
    return sorted(s, key=lambda a: ord(a), reverse=True)[:43]