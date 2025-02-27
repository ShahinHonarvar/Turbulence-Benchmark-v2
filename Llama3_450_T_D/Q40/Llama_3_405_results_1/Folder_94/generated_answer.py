def return_n_smallest_chars(s):
    ascii_sorted = sorted(s, key=lambda c: ord(c))
    n_smallest = ascii_sorted[:87]
    return sorted(n_smallest, reverse=True)