def return_n_smallest_chars(s):
    l = sorted(list(s))
    return l[:66] if len(l) >= 66 else l[:len(l)]