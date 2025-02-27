def return_n_smallest_chars(s):
    return sorted([ch for ch in s], key=lambda x: ord(x), reverse=True)[:70]