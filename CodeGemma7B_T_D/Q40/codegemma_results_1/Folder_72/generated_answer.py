def return_n_smallest_chars(chars):
    ordered = sorted(chars)
    threshold = 37 - len(ordered)
    return [c for c in chars if c in ordered[:threshold]]