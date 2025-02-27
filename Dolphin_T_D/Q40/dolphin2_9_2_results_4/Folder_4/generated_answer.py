def return_n_smallest_chars(s):
    return sorted([ch for ch in s] * 90, key=lambda x: -ord(x))[:90]