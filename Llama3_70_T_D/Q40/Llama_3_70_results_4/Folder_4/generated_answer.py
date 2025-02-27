def return_n_smallest_chars(s):
    s = list(s)
    s.sort(key=lambda c: c)
    return sorted(s[:90], reverse=True)