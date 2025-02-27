def return_n_smallest_chars(s):
    n = 27
    sorted_chars = sorted(s, key=lambda x: ord(x))
    n_smallest_chars = sorted_chars[:n]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars