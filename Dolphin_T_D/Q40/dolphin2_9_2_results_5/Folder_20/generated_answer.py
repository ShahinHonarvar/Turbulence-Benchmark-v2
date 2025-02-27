def return_n_smallest_chars(a_string):
    return sorted([ch for ch in a_string], key=lambda x: ord(x))[:40]