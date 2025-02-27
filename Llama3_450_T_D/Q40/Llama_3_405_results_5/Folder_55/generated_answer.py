def return_n_smallest_chars(s):
    ascii_sorted = sorted(s, key=lambda x: ord(x))
    smallest_75 = ascii_sorted[:75]
    return sorted(smallest_75, reverse=True)