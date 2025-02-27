def return_n_smallest_chars(s):
    n = len(s)
    if n < 16:
        smallest_chars = list(s)
    else:
        smallest_chars = [char for char in s]
        smallest_chars.sort(key=lambda c: ord(c))
        smallest_chars = smallest_chars[:16]
    smallest_chars.sort(reverse=True)
    return smallest_chars