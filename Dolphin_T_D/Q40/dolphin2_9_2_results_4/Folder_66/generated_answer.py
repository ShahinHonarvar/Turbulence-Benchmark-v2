def return_n_smallest_chars(s):
    ascii_vals = [ord(c) for c in s]
    smallest_chars = sorted(ascii_vals)[:33]
    sorted_chars = sorted(s, key=lambda c: ord(c), reverse=True)[:33]
    return sorted_chars