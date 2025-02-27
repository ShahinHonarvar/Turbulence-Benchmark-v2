def return_n_smallest_chars(s):
    return sorted(s[:24], key=lambda x: -ord(x))