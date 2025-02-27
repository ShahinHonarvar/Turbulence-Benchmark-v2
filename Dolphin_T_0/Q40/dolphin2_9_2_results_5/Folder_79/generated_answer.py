def return_n_smallest_chars(s):
    ordered_chars = [c for c in s]
    ordered_chars.sort()
    ordered_chars = ordered_chars[:82]
    ordered_chars.sort(reverse=True)
    return ordered_chars