def return_n_smallest_chars(s):
    return sorted([c for c in s], key=lambda x: ord(x))[::-1][:6]