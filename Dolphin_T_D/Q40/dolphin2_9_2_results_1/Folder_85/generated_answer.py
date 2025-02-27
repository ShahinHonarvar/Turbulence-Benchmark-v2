def return_n_smallest_chars(s):
    ch = [c for c in s]
    ch.sort()
    return ch[:85][::-1]