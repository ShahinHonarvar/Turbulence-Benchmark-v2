def return_n_smallest_chars(s):
    sorted_chars = sorted([c for c in s], key=lambda c: ord(c))
    return sorted(sorted_chars[:24], key=lambda c: -ord(c))