def return_n_greatest_chars(s):
    sorted_chars = sorted([c for c in s])
    return sorted([c for c in sorted_chars if ord(c) >= ord(sorted_chars[-38])])