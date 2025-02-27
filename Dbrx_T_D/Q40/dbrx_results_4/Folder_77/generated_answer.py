def return_n_smallest_chars(s):
    ascii_sorted = sorted((ord(c) for c in s))
    return [chr(i) for i in ascii_sorted[:47]]