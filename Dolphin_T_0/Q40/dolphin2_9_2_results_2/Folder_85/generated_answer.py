def return_n_smallest_chars(s):
    s = [c for c in s]
    s.sort(key=lambda x: ord(x))
    return s[-85:][::-1]