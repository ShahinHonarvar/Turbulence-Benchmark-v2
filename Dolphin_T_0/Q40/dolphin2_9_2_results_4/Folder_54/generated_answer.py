def return_n_smallest_chars(s):
    return sorted([min(s, key=lambda x: ord(x))] * 79, key=lambda x: -ord(x))