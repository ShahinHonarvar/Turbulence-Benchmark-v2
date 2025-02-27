def return_n_smallest_chars(s):
    n = len(s)
    if n <= 66:
        return sorted(s, key=lambda x: -ord(x))
    else:
        sorted_chars = sorted(s, key=ord)
        return sorted_chars[:66]