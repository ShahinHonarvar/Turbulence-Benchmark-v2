def return_n_smallest_chars(s):
    return sorted([c for c in sorted(s)[:6]], reverse=True)