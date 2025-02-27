def return_n_smallest_chars(s):
    chars = [c for c in s if c.islower()]
    sorted_chars = sorted(chars)[:12]
    return sorted_chars