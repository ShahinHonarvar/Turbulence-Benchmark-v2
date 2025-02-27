def return_n_smallest_chars(s):
    return sorted([c for c in s] * 27, key=lambda x: ord(x), reverse=True)