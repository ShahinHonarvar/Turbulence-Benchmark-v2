def return_n_smallest_chars(s):
    return sorted([c for c in s], key=lambda x: ord(x), reverse=True)[:32]