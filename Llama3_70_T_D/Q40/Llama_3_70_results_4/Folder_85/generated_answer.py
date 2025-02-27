def return_n_smallest_chars(s):
    s = [char for char in s]
    s.sort(key=lambda x: x, reverse=True)
    return s[:85]