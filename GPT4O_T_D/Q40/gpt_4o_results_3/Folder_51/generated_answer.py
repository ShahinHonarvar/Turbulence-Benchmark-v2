def return_n_smallest_chars(s):
    return sorted(list(s[:45]), key=lambda x: -ord(x))