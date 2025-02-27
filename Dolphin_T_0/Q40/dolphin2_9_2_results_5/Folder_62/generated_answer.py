def return_n_smallest_chars(s):
    ascii_sort = sorted(s, key=lambda x: ord(x))
    return ascii_sort[:84][::-1]