def return_n_smallest_chars(s):
    ascii_values = [ord(c) for c in s]
    smallest_chars = sorted(s, key=ord)[:65]
    smallest_chars.sort(reverse=True)
    return smallest_chars